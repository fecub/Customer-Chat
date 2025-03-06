from datetime import datetime

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from core.database.session import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)  # "customer" oder "support"

    chats = relationship("ChatSession", back_populates="customer", foreign_keys="[ChatSession.customer_id]")
    support_chats = relationship("ChatSession", back_populates="support", foreign_keys="[ChatSession.support_id]")
