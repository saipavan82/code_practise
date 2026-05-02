from fastapi import FastAPI

app = FastAPI()

@app.get("/get-name/{name}")
def get_name(name: str):
    return {
        "message": f"Hello, {name}"
    }