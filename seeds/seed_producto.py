import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.db import SessionLocal
from models.producto import Producto

def seed_productos():
    db = SessionLocal()
    productos = [
        Producto(nombre="Detergente", categoria="Limpieza", precio=1500),
        Producto(nombre="Desinfectante", categoria="Limpieza", precio=2000),
        Producto(nombre="Escoba", categoria="Accesorios", precio=1200),
        Producto(nombre="Cloro", categoria="Limpieza", precio=1000),
    ]
    for producto in productos:
        db.add(producto)
    db.commit()
    db.close()

if __name__ == "__main__":
    seed_productos()
