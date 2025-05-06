<<<<<<< HEAD
import gensim
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

# Load the model
model = gensim.models.KeyedVectors.load('model/model.mdl')

app = FastAPI()

# Request body model
class SimilarityRequest(BaseModel):
    word1: str
    word2: str

@app.get("/similarity")
def get_similarity(request: SimilarityRequest):
    word1 = request.word1
    word2 = request.word2
    try:
        # Calculate the cosine similarity
        similarity = model.similarity(word1, word2)
        return {"word1": word1, "word2": word2, "similarity": similarity}
    except KeyError:
        return {"error": "One or both words not in vocabulary."}
=======
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from gensim.models import Word2Vec
import uvicorn

app = FastAPI()

# טען את המודל המאומן
model = Word2Vec.load("model.mdl")

class WordPair(BaseModel):
    word1: str
    word2: str

@app.post("/similarity")
def get_similarity(pair: WordPair):
    if pair.word1 not in model.wv or pair.word2 not in model.wv:
        raise HTTPException(status_code=404, detail="אחת המילים לא קיימת במודל")
    
    similarity = model.wv.similarity(pair.word1, pair.word2)
    return {"similarity": similarity}
>>>>>>> ab13467 (initial commit)
