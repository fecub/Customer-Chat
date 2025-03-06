from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


class ChatSessionBase(BaseModel):
    customer_id: int
    customer_name: Optional[str]


class ChatSessionCreate(ChatSessionBase):
    pass


class ChatSessionResponse(ChatSessionBase):
    id: int
    support_id: Optional[int]
    status: str
    created_at: datetime

    class Config:
        from_attributes = True


class MessageBase(BaseModel):
    chat_id: int
    sender_id: int
    content: str


class MessageCreate(MessageBase):
    pass


class MessageResponse(MessageBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True
