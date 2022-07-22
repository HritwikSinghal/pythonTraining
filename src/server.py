# import FastAPI
from fastapi import FastAPI

# create a FastAPI instance
app = FastAPI()


# create a path operation
@app.get("/")
# define the path operation function
def root():
    return {"message": "Hello World"}


def start():
    pass
