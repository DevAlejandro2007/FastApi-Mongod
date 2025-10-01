Aquí tienes un **esqueleto profesional** para tu proyecto FastAPI + MongoDB. Lo puedes usar como base y adaptarlo a tu código actual.

---

## 📂 Estructura recomendada del proyecto

```
FastApi-Mongod/
├─ api/
│  ├─ main.py              # Punto de entrada de la app (FastAPI instance)
│  ├─ routers/             # Rutas (endpoints)
│  │   ├─ __init__.py
│  │   ├─ items.py
│  │   └─ users.py
│  ├─ schemas/             # Modelos Pydantic (validación de entrada/salida)
│  │   ├─ __init__.py
│  │   ├─ item_schema.py
│  │   └─ user_schema.py
│  ├─ services/            # Lógica de negocio / CRUD
│  │   ├─ __init__.py
│  │   ├─ item_service.py
│  │   └─ user_service.py
│  ├─ models/              # Modelos de DB si decides usarlos (ej: ODM)
│  │   └─ __init__.py
│  ├─ core/                # Configuración y utilidades base
│  │   ├─ __init__.py
│  │   ├─ config.py        # Configuración con Pydantic BaseSettings
│  │   └─ security.py      # Manejo de JWT, hashing, etc (si lo agregas)
│  ├─ db.py                # Conexión a MongoDB (Motor)
│  └─ utils/               # Funciones auxiliares
│      └─ __init__.py
├─ tests/                  # Pruebas con pytest
│  ├─ __init__.py
│  ├─ test_items.py
│  └─ test_users.py
├─ .env.example            # Variables de entorno de ejemplo
├─ requirements.txt        # Dependencias principales
├─ requirements-dev.txt    # Dependencias para desarrollo y testing
├─ README.md               # Documentación del proyecto
└─ .gitignore
```

---

## 📝 Ejemplo de archivos clave

### `api/main.py`

```python
from fastapi import FastAPI
from .routers import items, users

app = FastAPI(title="FastApi-Mongod")

# Registrar routers
app.include_router(items.router, prefix="/items", tags=["items"])
app.include_router(users.router, prefix="/users", tags=["users"])

@app.get("/")
async def root():
    return {"message": "Bienvenido a FastApi-Mongod 🚀"}
```

### `api/core/config.py`

```python
from pydantic import BaseSettings

class Settings(BaseSettings):
    MONGODB_URI: str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "fastapi_db"
    SECRET_KEY: str = "supersecret"

    class Config:
        env_file = ".env"

settings = Settings()
```

### `api/db.py`

```python
from motor.motor_asyncio import AsyncIOMotorClient
from .core.config import settings

client = AsyncIOMotorClient(settings.MONGODB_URI)
db = client[settings.DATABASE_NAME]
```

### `api/routers/items.py`

```python
from fastapi import APIRouter, HTTPException
from ..schemas.item_schema import Item
from ..services.item_service import get_items, create_item

router = APIRouter()

@router.get("/", response_model=list[Item])
async def list_items():
    return await get_items()

@router.post("/", response_model=Item)
async def add_item(item: Item):
    new_item = await create_item(item)
    if not new_item:
        raise HTTPException(status_code=400, detail="No se pudo crear el item")
    return new_item
```

### `api/schemas/item_schema.py`

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
```

### `api/services/item_service.py`

```python
from ..db import db
from ..schemas.item_schema import Item

collection = db["items"]

async def get_items():
    items = await collection.find().to_list(100)
    return items

async def create_item(item: Item):
    result = await collection.insert_one(item.dict())
    if result.inserted_id:
        return {"id": str(result.inserted_id), **item.dict()}
    return None
```

### `tests/test_items.py`

```python
import pytest
from httpx import AsyncClient
from api.main import app

@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenido a FastApi-Mongod 🚀"}
```

