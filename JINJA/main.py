from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

languages = [
    {"id": 1, "name": "Python"},
    {"id": 2, "name": "Rust"},
    {"id": 3, "name": "JavaScript"}
]

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html.jinja",
        {
            "request": request,
            "languages": languages
        }
    )

@app.get("/language/{id}", response_class=HTMLResponse)
async def language_detail(request: Request, id: int):
    language = next((l for l in languages if l["id"] == id), None)

    return templates.TemplateResponse(
        "language.html.jinja",
        {
            "request": request,
            "language": language
        }
    )
