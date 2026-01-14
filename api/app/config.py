# app/config.py
import os
import pymongo
from fastapi.templating import Jinja2Templates

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

MONGO_URI = "mongodb://localhost:27017/"
NOMBRE_DATABASE = "api"
MONGO_COLECCION = "user"

try:
    cliente = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=2000)
    cliente.server_info()
    print("✅ Conectado a MongoDB")
    base_datos = cliente[NOMBRE_DATABASE]
    COLECCION = base_datos[MONGO_COLECCION]
except Exception as e:
    print("⛔ Error conectando a MongoDB:", e)
    COLECCION = None
    