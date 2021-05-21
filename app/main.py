
from fastapi import FastAPI
from .helper import process, phrases

app = FastAPI()


@app.get("/similarity/")
def compare_strings(s1: str, s2: str):
	return {'similarity': process(s1, s2)}


@app.get('/sim_by_id/')
def compare_strings_by_id(id1: int, id2: int):
	# id provided should start at 1
	id1 -= 1
	id2 -= 1
	return {'similarity': process(phrases[id1], phrases[id2])}