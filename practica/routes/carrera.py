from model import Carrera
from fastapi import APIRouter


carrera_router = APIRouter()

@carrera_router.get("/carrera")
async def get_carreras() -> dict:
    return {"carreras": carrera_list}