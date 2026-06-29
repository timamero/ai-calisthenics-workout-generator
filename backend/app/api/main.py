from fastapi import APIRouter

from .routes import generate_workout

api_router = APIRouter()
api_router.include_router(generate_workout.router)
