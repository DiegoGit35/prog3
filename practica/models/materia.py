from pydantic import BaseModel

class Materia(BaseModel):
    id: int
    nombre: str
    duracion: int


    class Config:
        schema_extra ={
            "example": {
                "nombre": "Matemática I",
                "duracion": 60
            }
        }
