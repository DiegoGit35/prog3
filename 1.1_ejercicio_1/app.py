from fastapi import FastAPI

app = FastAPI()

stores = [{"name": "My Store", "items": [{"name": "my item", "price": 15.99}]}]

@app.get("/stores")
async def get_stores() -> dict:
    return {"stores": stores}

@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}