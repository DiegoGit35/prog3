from fastapi import FastAPI
# from fastapi import APIRouter
from todo import todo_router
from model import Todo

app = FastAPI()
# router = APIRouter()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}


app.include_router(todo_router)


# @router.get("/hello")
# async def say_hello() -> dict:
#     return {"message": "Hello!"}