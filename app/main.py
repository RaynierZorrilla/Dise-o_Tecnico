from fastapi import FastAPI
from app.api import tasks
from app.db.base import Base
from app.db.session import engine

# Crear las tablas
Base.metadata.create_all(bind=engine)

# Crear la aplicación FastAPI
app = FastAPI()

# Ruta raíz
@app.get("/")
def read_root():
    return {"message": "¡Bienvenido a tu gestor de tareas!"}

# Incluir las rutas de las tareas
app.include_router(tasks.router, prefix="/api", tags=["tasks"])
