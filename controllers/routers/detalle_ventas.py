from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.db import SessionLocal
from models.detalle_venta import DetalleVenta
from typing import List
from datetime import datetime
from models.schemas import DetalleVentaSchema

router = APIRouter(
    prefix="/detalle_ventas", tags=["Detalle Ventas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#obtener todos los detalles de ventas
@router.get("/", response_model=List[DetalleVentaSchema])
def listar_detalle_ventas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    detalles = db.query(DetalleVenta).offset(skip).limit(limit).all()
    return detalles

#obtener detalle de venta por id
@router.get("/{detalle_id}", response_model=DetalleVentaSchema)
def obtener_detalle_venta(detalle_id: int, db: Session = Depends(get_db)) -> DetalleVentaSchema:
    detalle = db.query(DetalleVenta).filter(DetalleVenta.id == detalle_id).first()
    if not detalle:
        raise HTTPException(status_code=404, detail="Detalle de venta no encontrado")
    return detalle

#crear nuevo detalle de venta
@router.post("/", response_model=DetalleVentaSchema)
def crear_detalle_venta(venta_id: int, producto_id: int, cantidad: int, precio: float, descuento: float = 0.0, db: Session = Depends(get_db)):
    nuevo_detalle = DetalleVenta(venta_id=venta_id, producto_id=producto_id, cantidad=cantidad, precio=precio, descuento=descuento)
    db.add(nuevo_detalle)
    db.commit()
    db.refresh(nuevo_detalle)
    return nuevo_detalle

#actualizar detalle de venta
@router.put("/{detalle_id}", response_model=DetalleVentaSchema)
def actualizar_detalle_venta(detalle_id: int, cantidad: int, precio: float, descuento: float = 0.0, db: Session = Depends(get_db)):
    detalle = db.query(DetalleVenta).filter(DetalleVenta.id == detalle_id).first()
    if not detalle:
        raise HTTPException(status_code=404, detail="Detalle de venta no encontrado")
    detalle.cantidad = cantidad
    detalle.precio = precio
    detalle.descuento = descuento
    db.commit()
    db.refresh(detalle)
    return detalle

#eliminar detalle de venta
@router.delete("/{detalle_id}")
def eliminar_detalle_venta(detalle_id: int, db: Session = Depends(get_db)):
    detalle = db.query(DetalleVenta).filter(DetalleVenta.id == detalle_id).first()
    if not detalle:
        raise HTTPException(status_code=404, detail="Detalle de venta no encontrado")
    db.delete(detalle)
    db.commit()
    return {"detail": "Detalle de venta eliminado"}