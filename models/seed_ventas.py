from services.db import SessionLocal
from models.cliente import Cliente
from models.producto import Producto
from models.ventas import Venta
from models.detalle_venta import DetalleVenta
from datetime import datetime
import random

def seed_ventas_y_detalles_realistas():
    db = SessionLocal()
    clientes = db.query(Cliente).all()
    productos = db.query(Producto).all()

    for cliente in clientes:
        num_ventas = random.randint(1, 50)  # Cada cliente tendrá entre 1 y 50 ventas
        for _ in range(num_ventas):
            venta = Venta(cliente_id=cliente.id, fecha=datetime.utcnow(), total=0)
            db.add(venta)
            db.flush()  # Para obtener el id de la venta

            productos_en_venta = random.sample(productos, k=random.randint(1, min(4, len(productos))))
            for producto in productos_en_venta:
                cantidad = random.randint(1, 50)
                # Lógica de descuentos escalonados
                if cantidad >= 15:
                    descuento = 0.25  # 25% de descuento
                elif cantidad >= 10:
                    descuento = 0.20  # 20% de descuento
                elif cantidad >= 5:
                    descuento = 0.15  # 15% de descuento
                else:
                    descuento = 0.0   # Sin descuento

                precio_unitario = producto.precio
                precio_final = precio_unitario * (1 - descuento)
                detalle = DetalleVenta(
                    venta_id=venta.id,
                    producto_id=producto.id,
                    cantidad=cantidad,
                    precio=precio_final,
                    descuento=descuento
                )
                db.add(detalle)
                venta.total += precio_final * cantidad

    db.commit()
    db.close()

if __name__ == "__main__":
    seed_ventas_y_detalles_realistas()
