from sqlalchemy import Integer, String, Column, DateTime
import uuid
from services.db import Base   
from datetime import datetime

class Cliente(Base):
    __tablename__ = "clientes"
    id  = Column(Integer, primary_key=True, index=True)
    uuid = Column(String(36), unique=True, default=lambda: str(uuid.uuid4()), index=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String, unique=True, nullable=False)
    rut = Column(String(20), unique=True, nullable=False)
    created_at = Column(DateTime, index=True, default=datetime.utcnow)
    updated_at = Column(DateTime, index=True, default=datetime.utcnow, onupdate=datetime.utcnow)