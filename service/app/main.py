from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.messages.routers import router as api_router

def create_app() -> FastAPI:
    app = FastAPI(title="API Service", version="0.0.1")
    # CORS
    origins = [
        "http://localhost",
        "http://localhost:8001",
        "http://localhost:8001/persistence/id"
    ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    # Routes
    app.include_router(api_router, prefix="/api")

    return app

app = create_app()