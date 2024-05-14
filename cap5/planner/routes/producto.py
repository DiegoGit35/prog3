
from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional

from models.producto import Producto

producto_router = APIRouter(
    tags=["productos"]
    )

productos = []

@producto_router.get("/{id}/stock")
async def obtener_stock(id: int):
    producto = check_producto_existe(id)
    return {"stock": producto.stock, "bajo_stock_minimo": producto.stock < producto.stock_minimo, "activo": producto.activo}

@producto_router.get("", response_model=List[Producto])
async def listar_productos():
    return productos

@producto_router.get("/{id}", response_model=Producto)
async def obtener_producto(id: int):
    producto = check_producto_existe(id)
    return producto

@producto_router.post("", response_model=Producto)
async def crear_producto(producto: Producto):
    if(next((p for p in productos if p.id == producto.id), None) is None):
        productos.append(producto)
        return producto
    else:
        raise HTTPException(status_code=409, detail="id en uso")

@producto_router.put("/{id}", response_model=Producto)
async def modificar_producto(id: int, producto_data: Producto):
    
    producto = check_producto_existe(id)

    producto_data.id = id
    productos.remove(producto)
    productos.append(producto_data)
    return producto_data

@producto_router.put("/{id}/desactivar")
async def desactivar_producto(id: int):
    producto = check_producto_existe(id)
    producto.activo = False
    return producto


def check_producto_existe(id: int):
    producto = next((p for p in productos if p.id == id), None)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto
