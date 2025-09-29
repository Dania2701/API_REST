from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.db import SessionLocal
from models.cliente import Cliente    
from typing import List
from datetime import datetime
from models.schemas import ClienteSchema

router = APIRouter(
    prefix="/clientes", tags=["Clientes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#obtener todos los clientes
@router.get("/", response_model=List[ClienteSchema])
def listar_clientes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    clientes = db.query(Cliente).offset(skip).limit(limit).all()
    return clientes

#obtener cliente por id
@router.get("/{cliente_id}", response_model=ClienteSchema)
def obtener_cliente(cliente_id: int, db: Session = Depends(get_db)) -> ClienteSchema:
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

#crear nuevo cliente
@router.post("/", response_model=ClienteSchema)
def crear_cliente(nombre: str, email: str, rut: str, db: Session = Depends(get_db)):
    nuevo_cliente = Cliente(nombre=nombre, email=email, rut=rut)
    db.add(nuevo_cliente)
    db.commit()
    db.refresh(nuevo_cliente)
    return nuevo_cliente

#actualizar cliente
@router.put("/{cliente_id}", response_model=ClienteSchema)
def actualizar_cliente(cliente_id: int, nombre: str, email: str, rut: str, db: Session = Depends(get_db)):
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    cliente.nombre = nombre
    cliente.email = email
    cliente.rut = rut
    db.commit()
    db.refresh(cliente)
    return cliente

#eliminar cliente
@router.delete("/{cliente_id}")
def eliminar_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    db.delete(cliente)
    db.commit()
    return {"detail": "Cliente eliminado"}