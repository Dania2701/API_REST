import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from seed_producto import seed_productos
from seed_cliente import seed_clientes
from seed_ventas import seed_ventas_y_detalles

if __name__ == "__main__":
    print("Creando productos...")
    seed_productos()
    print("Productos creados")

    print("Creando clientes...")
    seed_clientes()
    print("Clientes creados")

    print("Creando ventas y detalles...")
    seed_ventas_y_detalles()
    print("Ventas y detalles creados")

    print("Base de datos poblada con datos de ejemplo")
