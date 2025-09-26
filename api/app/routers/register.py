from fastapi import APIRouter, Request, Form
from fastapi.responses import JSONResponse, HTMLResponse
from config import templates, COLECCION

router = APIRouter(
    prefix="/register",
    tags = ["Register"],
responses={404: {"MESSAGE": "Página no encontrada"}}
)

@router.get("/", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse("register.html",{"request": request})

@router.post("/",response_class=JSONResponse)
async def register_action(fullname: str=Form(...),email:str=Form(...),username: str= Form(...), password: str= Form(...)):
    if COLECCION is None:
        return JSONResponse(status_code=500, content={"error":"BASE DE DATOS NO DISPONIBLE"})
    try:
        usuario = COLECCION.find_one({"nombre":username})
        if usuario:
            return JSONResponse(status_code=400, content={"error": "USUARIO YA EXISTE"})
        user = {"username":username,"password":password,"email":email,"nombre":fullname }
        result =COLECCION.insert_one(user)
        return JSONResponse(
            status_code=201,
            content={
                "message": "Usuario creado exitosamente",
                "user_id": str(result.inserted_id),
                "usuario": {
                    "nombre": username,
                    "fullname": fullname
                }
            }
        )
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"error en el registro: {str(e)}"})