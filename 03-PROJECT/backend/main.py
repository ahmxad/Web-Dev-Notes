from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="../frontend")

app.mount("/assets", StaticFiles(directory="../frontend/assets"), name="assets")
app.mount("/static", StaticFiles(directory="../frontend/static"), name="static")

@app.get("/")
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/about")
def about(request: Request):
    return templates.TemplateResponse("pages/about.html", {"request": request})
