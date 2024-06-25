from pydantic import BaseModel
from typing import Optional, List
from sqlmodel import SQLModel, Field, Column
from models.carrera import Carrera

class Alumno(SQLModel, table=True):
    id: int = Field(default = None, primary_key=True)
    nombre: str
    apellido: str
    dni: int
    carreras: Optional[List[Carreras]] = Field(sa_column=Column(JSON))

    
    class Config:
        schema_extra = {
            "example": {
                "nombre": "Pedro",
                "apellido": "Fernandez",
                "dni": 93912388,
                "carreras": []
            }
        }