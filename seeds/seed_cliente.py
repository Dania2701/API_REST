import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.db import SessionLocal
from models.cliente import Cliente

def seed_clientes():
    db = SessionLocal()
    clientes = [
        Cliente(nombre="Juan Pérez", email="juan.perez@email.com", rut="12345678-9"),
        Cliente(nombre="Ana Gómez", email="ana.gomez@email.com", rut="98765432-1"),
        Cliente(nombre="Carlos Ruiz", email="carlos.ruiz@email.com", rut="11223344-5"),
        Cliente(nombre="Juan Suazo", email="juan.suazo@email.com", rut="22334455-6"),
        Cliente(nombre="Maria Rodriguez", email="maria.rodriguez@email.com", rut="33445566-7"),
        Cliente(nombre="Mario Castro", email="mario.castro@email.com", rut="44556677-8"),
    ]
    for cliente in clientes:
        db.add(cliente)
    db.commit()
    db.close()

if __name__ == "__main__":
    seed_clientes()
