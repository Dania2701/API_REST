from services.db import SessionLocal
from models.cliente import Cliente
from models.producto import Producto
from models.ventas import Venta
from models.detalle_venta import DetalleVenta

# Mostrar resumen de ventas por producto
def resumen_ventas_por_producto():
    db = SessionLocal()
    print("Ventas por producto:")
    productos = db.query(Producto).all()
    for producto in productos:
        total_vendido = db.query(DetalleVenta).filter(DetalleVenta.producto_id == producto.id).count()
        print(f"- {producto.nombre}: {total_vendido} ventas")
    db.close()

# Mostrar resumen de compras por cliente
def resumen_compras_por_cliente():
    db = SessionLocal()
    print("Compras por cliente:")
    clientes = db.query(Cliente).all()
    for cliente in clientes:
        total_compras = db.query(Venta).filter(Venta.cliente_id == cliente.id).count()
        print(f"- {cliente.nombre}: {total_compras} compras")
    db.close()

if __name__ == "__main__":
    resumen_ventas_por_producto()
    print()
    resumen_compras_por_cliente()
