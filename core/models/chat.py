from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

from core.database.session import Base


class ChatSession(Base):
    __tablename__ = "chat_sessions"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("users.id"))
    support_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    status = Column(String, default="open")  # "open", "closed"
    created_at = Column(DateTime, default=datetime.utcnow)

    customer = relationship("User", foreign_keys=[customer_id], back_populates="chats")
    support = relationship("User", foreign_keys=[support_id], back_populates="support_chats")
    messages = relationship("Message", back_populates="chat")

    @hybrid_property
    def customer_name(self):
        return self.customer.name if self.customer else None


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(Integer, ForeignKey("chat_sessions.id"))
    sender_id = Column(Integer, ForeignKey("users.id"))
    content = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    chat = relationship("ChatSession", back_populates="messages")
