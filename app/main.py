from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.firebase import db
from app.routers import users, matches, predictions

app = FastAPI(
    title="Polla Mundialista API",
    description="Backend para la plataforma de predicciones del Mundial 2026",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(matches.router)
app.include_router(predictions.router)

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Polla Mundialista API corriendo"}
