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
    return {
        "GET /help": "GET request on '/help' to Show this help. (curl http://localhost/help)",
        "GET /show": "GET request on '/show' to Show DB. (curl http://localhost/show)",
        "GET / key=foo": "GET request on '/' to get 'foo' from DB. (curl http://localhost/?key=foo)",
        "PUT / key=foo value=bar": "PUT request on '/' to put 'foo' to DB. (curl -X PUT 'http://localhost/?key=foo&value=bar')",
        "DELETE key=foo": "DELETE request on '/' to delete 'foo' from DB (curl -X DELETE 'http://localhost:8080/?key=foo')"
    }


@app.get("/show")
async def show() -> dict:
    """returns Database
    :return Database:dict, the database in dict format
    """
    return my_db.show()


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
