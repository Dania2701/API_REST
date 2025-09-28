from sqlalchemy import Integer, String, Float, Column, DateTime
import uuid
from services.db import Base   
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class Producto(Base):
    __tablename__ = "productos"
    id : Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    uuid: Mapped[str] = mapped_column(String(36), unique=True, default=lambda: str(uuid.uuid4()), index=True)
    nombre : Mapped[str] = mapped_column(String, index=True)
    categoria : Mapped[str] = mapped_column(String, index=True)
    precio : Mapped[float] = mapped_column(Float, index=True)
    created_at = Column(DateTime, index=True, default=datetime.utcnow)