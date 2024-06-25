from sqlmodel import SQLModel, Field, Column
from models.materia import Materia

class Carrera(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nombre: str
    materias: List[Materia] = Field(sa_column=Column(JSON))

    class Config:
        schema_extra = {
            "example": {
                "nombre": "Tecnicatura en Desarrollo de Software",
                "marerias": []
            }
        }