from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProductoSchema(BaseModel):
    id: int
    uuid: str
    nombre: str
    categoria: str
    precio: float
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class ClienteSchema(BaseModel):
    id: int
    uuid: str
    nombre: str
    email: str
    rut: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class DetalleVentaSchema(BaseModel):
    id: int
    uuid: str
    venta_id: int
    producto_id: int
    cantidad: int
    precio: float
    descuento: float = 0.0
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class VentaSchema(BaseModel):
    id: int
    uuid: str
    cliente_id: int
    total: float
    fecha: datetime
    detalles: Optional[list[DetalleVentaSchema]] = []
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True