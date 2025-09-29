from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.db import SessionLocal
from models.ventas import Venta    
from typing import List
from datetime import datetime
from models.schemas import VentaSchema

router = APIRouter(
    prefix="/ventas", tags=["Ventas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#obtener todas las ventas
@router.get("/", response_model=List[VentaSchema])
def listar_ventas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    ventas = db.query(Venta).offset(skip).limit(limit).all()
    return ventas

#obtener venta por id
@router.get("/{venta_id}", response_model=VentaSchema)
def obtener_venta(venta_id: int, db: Session = Depends(get_db)) -> VentaSchema:
    venta = db.query(Venta).filter(Venta.id == venta_id).first()
    if not venta:
        raise HTTPException(status_code=404, detail="Venta no encontrada")
    return venta

#crear nueva venta
@router.post("/", response_model=VentaSchema)
def crear_venta(fecha: datetime, total: float, cliente_id: int, db: Session = Depends(get_db)):
    nueva_venta = Venta(fecha=fecha, total=total, cliente_id=cliente_id)
    db.add(nueva_venta)
    db.commit()
    db.refresh(nueva_venta)
    return nueva_venta

#actualizar venta
@router.put("/{venta_id}", response_model=VentaSchema)
def actualizar_venta(venta_id: int, fecha: datetime, total: float, cliente_id: int, db: Session = Depends(get_db)):
    venta = db.query(Venta).filter(Venta.id == venta_id).first()
    if not venta:
        raise HTTPException(status_code=404, detail="Venta no encontrada")
    venta.fecha = fecha
    venta.total = total
    venta.cliente_id = cliente_id
    db.commit()
    db.refresh(venta)
    return venta

#eliminar venta
@router.delete("/{venta_id}")
def eliminar_venta(venta_id: int, db: Session = Depends(get_db)):
    venta = db.query(Venta).filter(Venta.id == venta_id).first()
    if not venta:
        raise HTTPException(status_code=404, detail="Venta no encontrada")
    db.delete(venta)
    db.commit()
    return {"detail": "Venta eliminada"}