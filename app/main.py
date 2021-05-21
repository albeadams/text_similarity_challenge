
from fastapi import FastAPI
from .helper import process

app = FastAPI()


@app.get("/similarity/")
def compare_strings(s1: str, s2: str):
	return {'similarity': process(s1, s2)}
