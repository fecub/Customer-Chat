from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database.session import get_db
from core.schema import chat_schema
from core.models.chat import ChatSession, Message

chat = APIRouter()


@chat.post("/chats/", response_model=chat_schema.ChatSessionResponse)
def create_chat(chat: chat_schema.ChatSessionCreate, db: Session = Depends(get_db)):
    db_chat = ChatSession(customer_id=chat.customer_id)
    db.add(db_chat)
    db.commit()
    db.refresh(db_chat)
    return db_chat


@chat.post("/messages/", response_model=chat_schema.MessageResponse)
def send_message(message: chat_schema.MessageCreate, db: Session = Depends(get_db)):
    chat = db.query(ChatSession).filter(ChatSession.id == message.chat_id).first()
    if not chat or chat.status == "closed":
        raise HTTPException(status_code=400, detail="Chat not found or closed")

    db_message = Message(chat_id=message.chat_id, sender_id=message.sender_id, content=message.content)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message


@chat.get("/chats/{chat_id}/messages", response_model=List[chat_schema.MessageResponse])
def get_chat_messages(chat_id: int, db: Session = Depends(get_db)):
    return db.query(Message).filter(Message.chat_id == chat_id).all()


@chat.post("/chats/{chat_id}/close")
def close_chat(chat_id: int, db: Session = Depends(get_db)):
    chat = db.query(ChatSession).filter(ChatSession.id == chat_id).first()
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")

    chat.status = "closed"
    db.commit()
    return {"message": "Chat closed"}


@chat.get("/chats/active", response_model=List[chat_schema.ChatSessionResponse])
def get_active_chats(db: Session = Depends(get_db)):
    active_chats = db.query(ChatSession).filter(ChatSession.status == "open").all()
    return active_chats
