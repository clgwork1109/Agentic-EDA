# FastAPI entrypoint
# Placeholder for `main.py` — initializes FastAPI app and routes
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.datasets import router as dataset_router
from app.api.eda import router as eda_router

app = FastAPI(
    title="Explainable Agentic EDA Platform",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(dataset_router, prefix="/api/v1")
app.include_router(eda_router, prefix="/api/v1")


@app.get("/")
def health_check():
    return {
        "status": "running",
        "message": "Explainable Agentic EDA Backend is live"
    }
