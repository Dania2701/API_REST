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