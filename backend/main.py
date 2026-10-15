from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from pathlib import Path

from backend.agents.uiux_agent import generate_uiux
from backend.agents.frontend_agent import generate_frontend

app = FastAPI(title="AppForge AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

generated_folder = Path("generated")
generated_folder.mkdir(exist_ok=True)

app.mount("/generated", StaticFiles(directory="generated", html=True), name="generated")


class AppRequest(BaseModel):
    brief: str


@app.get("/")
def home():
    return {"message": "AppForge AI backend is running"}


@app.post("/generate")
def generate(request: AppRequest):

    uiux_result = generate_uiux(request.brief)

    frontend_result = generate_frontend(uiux_result)

    (generated_folder / "index.html").write_text(
        frontend_result["index_html"],
        encoding="utf-8"
    )

    (generated_folder / "style.css").write_text(
        frontend_result["style_css"],
        encoding="utf-8"
    )

    (generated_folder / "app.js").write_text(
        frontend_result["app_js"],
        encoding="utf-8"
    )

    return {
        "success": True,
        "message": "Frontend generated successfully",
        "preview_url": "http://127.0.0.1:8000/generated/index.html",
        "files": [
            "generated/index.html",
            "generated/style.css",
            "generated/app.js"
        ]
    }