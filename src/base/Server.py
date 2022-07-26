from fastapi import FastAPI, HTTPException
from . import Database
from .dbholder import DBHolder

# create a FastAPI instance
app = FastAPI()

# create a holder for my DB. This is to prevent use of Global variable with DB name
my_db_holder = DBHolder()


# create a path operation
@app.get("/")
# define the path operation function
async def help() -> dict:
    """returns all available commands to user"""
    return {
        "GET /": "GET request on '/' to Show this help. (curl http://localhost/)",
        "GET /api/v1/ key=foo": "GET request on '/api/v1/' to get 'foo' from DB. (curl http://localhost/api/v1/?key=foo)",
        "PUT /api/v1/ key=foo,value=bar": "PUT request on '/api/v1/' to put 'foo' in DB. (curl -X PUT 'http://localhost/api/v1/?key=foo&value=bar')",
        "GET /api/v1/show": "GET request on '/api/v1/show' to Show DB. (curl http://localhost/api/v1/show)",
        "DELETE /api/v1/delete key=foo": "DELETE request on '/api/v1/' to delete 'foo' from DB (curl -X DELETE 'http://localhost/api/v1/?key=foo')",
        "POST /api/v1/truncate i_am_sure=True": "POST request on '/api/v1/truncate' to empty the current DB (curl -X POST 'http://localhost/api/v1/truncate?i_am_sure=False')",
        "POST /api/v1/create db_name=foo": "POST request on '/api/v1/create' to create a DB named 'foo' (curl -X POST 'http://localhost/api/v1/create?db_name=foo')",
    }


@app.post("/api/v1/create")
async def create_DB(db_name: str) -> bool:
    try:
        my_db_holder.db = Database.Database(name=db_name)
        return True
    except:
        # log that shitt here.
        print(f"Something went wrong while creating the DB {db_name}")
        return False


@app.get("/api/v1/show")
async def show() -> dict:
    """returns Database
    :return Database:dict, the database in dict format
    """
    return my_db_holder.db.show()


@app.get("/api/v1/")
async def get(key: str) -> str:
    """get value of key from DB
    :param key, get the value of this key
    :return str, the message from DB
    """
    return my_db_holder.db.get(key)


@app.put("/api/v1/")
async def put(key: str, value: str) -> str:
    """Put key, value in DB
    :param key:str, key to be inserted
    :param value:str, value to be inserted for the key
    :return str, the message from DB
    """
    return my_db_holder.db.put(f"{key}={value}")


@app.delete("/api/v1/")
async def delete(key: str) -> str:
    """delete the key from DB
    :param key:str, Key to be deleted
    :return str, the message from DB
    """
    return my_db_holder.db.delete(key)


@app.post("/api/v1/truncate")
async def truncate(i_am_sure: bool) -> str:
    """Truncates the whole DB. BE VERY CAREFULL with thin
    :return the message from DB
    """
    if not i_am_sure:
        raise HTTPException(status_code=401,
                            detail="You need to be sure to truncate the DB. use 'i_am_sure=True'")
    return my_db_holder.db.truncate()
