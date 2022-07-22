# import FastAPI
import json

from fastapi import FastAPI
from . import Database

# create a FastAPI instance
app = FastAPI()

# todo: take location of DB
my_db = Database.Database()


# create a path operation
@app.get("/help")
# define the path operation function
async def root():
    return {
        "get X": "Get X from DB",
        "put X": "Put X to DB",
        "delete X": "Delete X from DB",
        "file": "Put values from file in DB",
        "show": "Show DB"
    }


@app.get("/show")
async def show_db():
    return my_db.show_db()


@app.get("/")
async def get(key: str):
    return my_db.get(key)


@app.put("/")
async def put(key: str, value: str):
    return my_db.put(f"{key}={value}")


@app.delete("/")
async def delete(key: str):
    return my_db.delete(key)
