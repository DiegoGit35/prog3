from typing import Optional
from pydantic import BaseModel, Field


class Producto(BaseModel):
    id: Optional[int] = None
    nombre: str = Field(min_length=1)
    categoria: str = Field(min_length=1)
    descripcion: str = Field(min_length=1, max_length=100)
    precio: float = Field(gt=0)

    # Atributos relacionados con el stock
    stock: int = Field(default=0, ge=0)
    stock_minimo: Optional[int] = None 
    stock_maximo: Optional[int] = None

    # Atributo de estado activo
    activo: bool = Field(default=True) 

    class Config:
        schema_extra = {
            'example': {
                'nombre': 'Silla',
                'categoria': 'Mueble',
                'descripcion': 'Una silla de escritorio',
                'precio': 90000.99,
                'stock': 10,
                'stock_minimo': 5, 
                'stock_maximo': 20, 
            }
        }