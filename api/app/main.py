from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from config import templates
from routers import login, register

app = FastAPI()

app.include_router(login.router)
app.include_router(register.router)

@app.get("/", response_class= HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})
