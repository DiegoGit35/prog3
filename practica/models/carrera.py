from pydantic import BaseModel
from models.materia import Materia

class Carrera(BaseModel):
    id: int
    nombre: str
    materias: List[Materia]

    class Config:
        schema_extra = {
            "example": {
                "nombre": "Tecnicatura en Desarrollo de Software",
                "marerias": []
            }
        }