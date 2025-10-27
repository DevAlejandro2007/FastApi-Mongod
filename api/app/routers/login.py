from fastapi import APIRouter, Request, Form
from fastapi.responses import JSONResponse, HTMLResponse
from config import templates, COLECCION

router = APIRouter(
    prefix="/login",        
    tags=["Login"],
    responses={404: {"message": "Página no encontrada"}}
)


# GET: Mostrar el formulario
@router.get("/", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# POST: Procesar login
@router.post("/", response_class=JSONResponse)
async def login_action(username: str = Form(...), password: str = Form(...)):
    if COLECCION is None:
        return JSONResponse(status_code=500, content={"error": "Base de datos no disponible"})

    try:
        usuario = COLECCION.find_one({"username": username, "password": password})
        if usuario:
            return {
                "message": "Login realizado",
                "usuario": {"id": str(usuario["_id"]), "nombre": usuario["nombre"]}
            }
        return JSONResponse(status_code=401, content={"error": "Credenciales incorrectas"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"Error en login: {str(e)}"})

