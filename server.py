from fastapi import FastAPI

server = FastAPI()


@server.get("/hello")
def hello():
    return {"message": "hello"}


@server.get("/bye")
def bye():
    return {"message": "bye!"}
