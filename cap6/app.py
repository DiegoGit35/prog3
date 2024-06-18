import SQLModel from sqlmodel
import 

class Libro(SQLModel, table=True):
    id: Optional[int] = Field(default=None, Primary_key=True)
    titulo: str
    autor: str
    descripcion: str
    genero: List[str]
