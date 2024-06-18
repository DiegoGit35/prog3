from pydantic import BaseModel
from typing import Optional
from models.carrera import Carrera

class Alumno(BaseModel):
    id: int
    nombre: str
    apellido: str
    dni: int
    carreras: Optional[List[Carreras]]
    
    class Config:
        schema_extra = {
            "example": {
                "nombre": "Pedro",
                "apellido": "Fernandez",
                "dni": 93912388,
                "carreras": []
            }
        }