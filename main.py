from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/")
def root():
    return {"message": "it works !"}


@app.get("/addition")
def addition(
    a: int = Query(..., description="First number"),
    b: int = Query(..., description="Second number"),
):
    return {"result a+b=": a + b, "developer": "Dev1"}