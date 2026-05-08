from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import generate, transform

app = FastAPI(title="JSON-CRAFTER", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(generate.router, prefix="/api")
app.include_router(transform.router, prefix="/api")


@app.get("/health")
def health():
    return {"status": "ok"}
