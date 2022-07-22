# import FastAPI
import json

from fastapi import FastAPI
from . import Database

# create a FastAPI instance
app = FastAPI()

# todo: take location of DB from a file or something
my_db = Database.Database()


# create a path operation
@app.get("/help")
# define the path operation function
async def help() -> dict:
    """returns all available commands to user"""
    # Todo : fix the help format to represent REST
    return {
        "get key=X": "Get X from DB",
        "put key=X, value=Y": "Put X to DB",
        "delete key=X": "Delete X from DB",
        "show": "Show DB"
    }


@app.get("/show")
async def show_db() -> dict:
    """returns DB
    :return Database:dict, the database in dict format
    """
    return my_db.show_db()


@app.get("/")
async def get(key: str) -> str:
    """get value of key from DB
    :param key, get the value of this key
    :return str, the message from DB
    """
    return my_db.get(key)


@app.put("/")
async def put(key: str, value: str) -> str:
    """Put key, value in DB
    :param key:str, key to be inserted
    :param value:str, value to be inserted for the key
    :return str, the message from DB
    """
    return my_db.put(f"{key}={value}")


@app.delete("/")
async def delete(key: str) -> str:
    """delete the key from DB
    :param key:str, Key to be deleted
    :return str, the message from DB
    """
    return my_db.delete(key)
