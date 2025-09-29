from sqlalchemy import Integer, String, Column, DateTime, ForeignKey, Float
from services.db import Base   
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid

class Venta(Base):
    __tablename__ = "ventas"
    id  = Column(Integer, primary_key=True, index=True)
    uuid = Column(String(36), unique=True, default=lambda: str(uuid.uuid4()), index=True)
    fecha = Column(DateTime, nullable=False, default=datetime.utcnow)
    total = Column(Float, nullable=False)
    created_at = Column(DateTime, index=True, default=datetime.utcnow)
    updated_at = Column(DateTime, index=True, default=datetime.utcnow, onupdate=datetime.utcnow)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    detalles = relationship("DetalleVenta", back_populates="venta", lazy="joined")