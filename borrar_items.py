from services.db import engine

with engine.connect() as conn:
    conn.execute("DROP TABLE IF EXISTS items;")
    print("Tabla 'items' eliminada correctamente.")