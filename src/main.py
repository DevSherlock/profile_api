from fastapi import FastAPI

app = FastAPI()


@app.get("/{name}")
async def root(name: str):
    return {"message": f"Hello, {name}!"}