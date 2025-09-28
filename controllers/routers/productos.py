from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.db import SessionLocal
from models.producto import Producto
from typing import List
from datetime import datetime
from models.schemas import ProductoSchema

router = APIRouter(
    prefix="/productos", tags=["Productos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#obtener todos los productos
@router.get("/", response_model=List[ProductoSchema])
def listar_productos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    productos = db.query(Producto).offset(skip).limit(limit).all()
    return productos

#listar productos por id
@router.get("/{producto_id}", response_model=ProductoSchema)
def obtener_producto(producto_id: int, db: Session = Depends(get_db)) -> ProductoSchema:
    producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

#agregar mas productos
@router.post("/", response_model=ProductoSchema)
def crear_producto(nombre: str, categoria: str, precio: float, db: Session = Depends(get_db)):
    nuevo_producto = Producto(nombre=nombre, categoria=categoria, precio=precio)
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto 

#actualizar productos
@router.put("/{producto_id}", response_model=ProductoSchema)
def actualizar_producto(producto_id: int, nombre: str, categoria: str, precio: float, db: Session = Depends(get_db)):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    producto.nombre = nombre
    producto.categoria = categoria
    producto.precio = precio
    db.commit()
    db.refresh(producto)
    return producto

#Eliminar productos
@router.delete("/{producto_id}")
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    db.delete(producto)
    db.commit()
    return {"message": "Producto eliminado exitosamente"}