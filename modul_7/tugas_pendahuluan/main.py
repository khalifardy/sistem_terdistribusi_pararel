from fastapi import FastAPI
import uvicorn
from mylib.logic import search_wiki
from mylib.logic import wiki as wikilogic
from mylib.logic import phrase as wikiphrases

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Wikipedia API.Call /search or /wiki"}


@app.get("/search/{value}")
async def search(value: str):
    """Mencari laman di WikiPedia"""
    result = search_wiki(value)
    return {"result": result}


@app.get("/wiki/{name}")
async def wiki(name: str):
    """Mengambil laman dari WikiPedia"""
    result = wikilogic(name)
    return {"result": result}


@app.get("/phrase/{name}")
async def phrase(name: str):
    """Mengambil laman dari WikiPedia dan mengembalikan kalimat"""
    result = wikiphrases(name)
    return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
