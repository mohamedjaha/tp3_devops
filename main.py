import socket
import platform
from fastapi import FastAPI, Query

app = FastAPI()


def get_local_ip():
    """Get the IP address of the network interface connected to the internet."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"


@app.get("/")
def root():
    return {"message": "it works !"}


@app.get("/addition")
def addition(
    a: int = Query(..., description="First number"),
    b: int = Query(..., description="Second number"),
):
    return {"result a+b=": a + b, "developer": "Dev1"}


@app.get("/greeting")
def greeting(name: str = Query(..., description="Name to greet")):
    return {
        "message": f"Hello, {name}",
        "developer": "Dev2",
        "hostname": platform.node(),
        "IP": get_local_ip(),
    }


@app.post("/divide")
def divide(
    a: int = Query(..., description="First number"),
    b: int = Query(..., description="Second number"),
):
    if b == 0:
        return {"error": "Division by zero is not allowed", "developer": "Dev4"}
    return {"result a/b=": a / b, "developer": "Dev4"}