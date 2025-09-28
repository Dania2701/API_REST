from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime, String
import uuid
from services.db import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class DetalleVenta(Base):
    __tablename__ = "detalle_venta"
    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String(36), unique=True, default=lambda: str(uuid.uuid4()), index=True)
    venta_id = Column(Integer, ForeignKey("ventas.id"), nullable=False)
    producto_id = Column(Integer, ForeignKey("productos.id"), nullable=False)
    cantidad = Column(Integer, nullable=False)
    precio = Column(Float, nullable=False)
    descuento = Column(Float, nullable=True, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    venta = relationship("Venta", back_populates="detalles")
    producto = relationship("Producto")
