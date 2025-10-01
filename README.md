![Static Badge](https://img.shields.io/badge/Python-3.13.2-blue?logo=Python&logoColor=blue), ![Static Badge](https://img.shields.io/badge/Git--orange?logo=Git&logoColor=orange), ![Static Badge](https://img.shields.io/badge/Github--grey?logo=Github&logoColor=black), ![Static Badge](https://img.shields.io/badge/FAST-API-brightgreen?style=flat&logo=Python)

# FastApi-Mongod

> Proyecto: API con FastAPI + MongoDB (Motor). Este repo es el primer proyecto del autor; este README propone una versión profesional, clara y lista para que otros desarrolladores lo usen y contribuyan.

---

## Tabla de contenidos

* [Descripción](#descripción)
* [Características](#características)
* [Tecnologías](#tecnologías)
* [Requisitos previos](#requisitos-previos)
* [Instalación (local)](#instalación-local)
* [Variables de entorno](#variables-de-entorno)
* [Ejecutar la aplicación](#ejecutar-la-aplicación)
* [Documentación de la API](#documentación-de-la-api)
* [Ejemplos de peticiones](#ejemplos-de-peticiones)
* [Tests](#tests)
* [Estructura recomendada del repo](#estructura-recomendada-del-repo)
* [Buenas prácticas y siguientes pasos](#buenas-prácticas-y-siguientes-pasos)
* [Contribuir](#contribuir)
* [Licencia](#licencia)

---

## Descripción

API construida con **FastAPI** y **MongoDB** (driver asíncrono *motor*). Proporciona endpoints REST para operar con la base de datos. Este README está pensado para que cualquier desarrollador pueda clonar, configurar y ejecutar el proyecto en su máquina.

> Nota: el archivo `base.py` es una guía interna del autor y se debe **ignorar** al revisar la lógica principal.

---

## Características

* Endpoints REST construidos con FastAPI
* Conexión asíncrona a MongoDB usando `motor`
* Documentación automática con Swagger UI y Redoc
* Estructura modular (routers, esquemas, servicios)

---

## Tecnologías

* Python 3.10+ (recomendado)
* FastAPI
* Uvicorn (servidor ASGI)
* Motor (MongoDB async driver)
* python-dotenv (variables de entorno)

---

## Requisitos previos

* Git
* Python 3.10 o superior
* MongoDB (local o en la nube: Atlas / MongoDB URI)

---

## Instalación (local)

1. Clona el repo:

```bash
git clone https://github.com/DevAlejandro2007/FastApi-Mongod.git
cd FastApi-Mongod
```

2. Crea y activa un entorno virtual (recomendado):

```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows
.\.venv\Scripts\activate
```

3. Instala dependencias:

```bash
pip install -r requirements.txt
```

4. Crea un archivo `.env` o exporta las variables necesarias (ver sección *Variables de entorno*).

---

## Variables de entorno

Crea un archivo `.env` en la raíz con al menos estas variables (ejemplo):

```
MONGODB_URI=mongodb://localhost:27017
DATABASE_NAME=fastapi_db
# Opcionales/útiles
SECRET_KEY=alguna-clave-secreta
HOST=0.0.0.0
PORT=8000
```

> Añade `.env` al `.gitignore` para no subir credenciales. Puedes incluir un `.env.example` en el repo con las claves sin valores reales.

---

## Ejecutar la aplicación

Si el punto de entrada de la aplicación es `main.py` en la raíz:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Si tu punto de entrada está dentro de la carpeta `api` (por ejemplo `api/main.py`):

```bash
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```

Ajusta la ruta si tu archivo se llama distinto. `--reload` es útil en desarrollo; no lo uses en producción.

---

## Documentación de la API

Una vez la app esté corriendo, FastAPI provee documentación automática:

* Swagger UI: `http://localhost:8000/docs`
* ReDoc: `http://localhost:8000/redoc`

Incluye un resumen corto de los endpoints en la sección *Estructura recomendada del repo*.

---

## Ejemplos de peticiones

Ejemplo `GET` a un endpoint `/items`:

```bash
curl -X GET "http://localhost:8000/items" -H "accept: application/json"
```

Ejemplo `POST` (JSON):

```bash
curl -X POST "http://localhost:8000/items" -H "Content-Type: application/json" -d '{"name":"ejemplo","price":10.5}'
```

Asegúrate de revisar los `schemas` (Pydantic) para los formatos esperados.

---

## Tests

Se recomienda incluir tests con `pytest` y `httpx` (cliente asíncrono) y `pytest-asyncio`.

Ejemplo (instalación de paquetes de desarrollo):

```bash
pip install -r requirements-dev.txt
pytest
```

---

## Estructura recomendada del repo

Sugerencia de organización para aumentar claridad y escalabilidad:

```
FastApi-Mongod/
├─ api/
│  ├─ main.py            # entrada de la app (FastAPI instance)
│  ├─ routers/           # routers por dominio (users, items, auth...)
│  ├─ services/          # lógica de negocio / CRUD
│  ├─ models/            # modelos Pydantic + modelos de DB si aplica
│  ├─ db.py              # conexión a Mongo (motor)
│  └─ utils/             # utilidades
├─ tests/
├─ .env.example
├─ requirements.txt
├─ requirements-dev.txt
├─ README.md
└─ .gitignore
```

---

## Buenas prácticas y siguientes pasos (priorizados)

1. **Documentación**: este README ya es una base; agrega ejemplos concretos de los endpoints más importantes.
2. **Config**: centralizar configuración con Pydantic `BaseSettings`.
3. **Seguridad**: nunca subir credenciales; considera autenticación (JWT) si la API lo requiere.
4. **Tests**: agrega tests unitarios y de integración.
5. **CI**: añade GitHub Actions para ejecutar `pytest` en PRs.
6. **Linting/formatting**: `black`, `ruff`/`flake8` y `isort`.

---

## Contribuir

1. Crea una issue para describir tu aporte.
2. Abre un branch (`git checkout -b feat/mi-cambio`).
3. Haz un PR con descripción clara.

---

## Licencia

Indica aquí la licencia del proyecto (por ejemplo MIT). Si no deseas publicar una licencia, remueve esta sección o añade `UNLICENSED`.

---

## Archivos sugeridos

A continuación agrego el contenido sugerido para `requirements.txt` y `requirements-dev.txt`. Guarda estos contenidos en archivos separados en la raíz del repo.

### requirements.txt (runtime)

```text
fastapi
uvicorn[standard]
motor
python-dotenv
```

### requirements-dev.txt (desarrollo / testing)

```text
pytest
pytest-asyncio
httpx
pytest-cov
black
ruff
```

---

## Cómo aplicar los cambios al repo (guía rápida)

```bash
# desde la raíz del repo
# 1) crear archivos
# (a) README.md -> pegar la sección README
# (b) requirements.txt -> pegar el bloque arriba
# (c) opcional: requirements-dev.txt y .env.example

git add README.md requirements.txt requirements-dev.txt .env.example
git commit -m "chore: improve README and add requirements files"
git push origin main
```

---

Si quieres, puedo:

* Generar el contenido listo para `README.md` y un `requirements.txt` como archivos descargables.
* Preparar el diff/patch para que puedas aplicar con `git apply`.
* Hacer una revisión específica del `api/` y adaptar el README con ejemplos reales de tus endpoints (para eso necesitaría que me confirmes el módulo de entrada: `main.py` o `api/main.py`).

Dime qué prefieres y continúo con el siguiente paso.
