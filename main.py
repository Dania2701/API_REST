from datetime import datetime
from fastapi import FastAPI
from sqlalchemy.orm import Session
from services.db import Base, engine, SessionLocal
from controllers.routers import productos
from controllers.routers import clientes
from controllers.routers import venta
from controllers.routers import detalle_ventas
from models.cliente import Cliente
from models.producto import Producto
from models.ventas import Venta
from models.detalle_venta import DetalleVenta

app = FastAPI(title="API productos de limpieza")

# prender evento
@app.on_event("startup")
def on_startup():
    # Crear la base de datos
    Base.metadata.create_all(bind=engine)
    # Crear una sesion de base de datos
    db: Session = SessionLocal()
    # Insertar datos semilla si la tabla está vacía

# inclusión de rutas de la api
app.include_router(productos.router)
app.include_router(clientes.router)
app.include_router(venta.router)
app.include_router(detalle_ventas.router)

@app.get("/")
def root():
    return {"status": "La API está funcionando", "docs": "/docs"}
