# API_REST

#API de Productos de Limpieza

Esta es una API REST desarrollada con *FastAPI* y *SQLAlchemy*, que gestiona productos, clientes, ventas y detalles de ventas.  
Incluye datos iniciales (*seeds*) para pruebas.

-----------------------------------------------------------------------------

#Requisitos e Instalación
1.-Clonar el repositorio
```bash
git clone https://github.com/Dania2701/API_REST.git
cd (entrar a la carpeta donde se clono o descargo el proyecto)

2.-Version de python 
3.9.1

3.-Instalar dependencias
pip install fastapi uvicorn sqlalchemy pydantic (instalar SQLite en extensiones en caso de no tener la extension con anterioridad)

4.-Levantar el servidor 
ejecutar comando en la terminal: uvicorn main:app --reload

#La API estara disponible por defecto en http://127.0.0.1:8000/ y la documentacion en http://127.0.0.1:8000/docs

5.-Cargar datos iniciales en la terminal: 
python seeds/seeds_all.py ---> #Esto creará registros de productos, clientes y ventas con detalles aleatorios

#Descripción de la Funcionalidad General. 

La API permite:
-Productos: listar, crear, actualizar y eliminar productos.
-Clientes: listar, crear, actualizar y eliminar clientes.
-Ventas: listar, registrar, actualizar y eliminar ventas asociadas a clientes.
-Detalles de venta: ver los productos vendidos en cada venta, con cantidad, precio y descuentos aplicados.

Esta API es ideal para simular un sistema de ventas básico en un negocio de productos de limpieza.

#Tecnologías Usadas

FastAPI – Framework para crear APIs rápidas.

SQLAlchemy – ORM para manejar la base de datos.

SQLite – Base de datos ligera para desarrollo.

Uvicorn – Servidor ASGI para correr la API.

#Finalmente, si se siguieron correctamente los pasos, se creara automaticamente una base de datos con el nombre "test.db"