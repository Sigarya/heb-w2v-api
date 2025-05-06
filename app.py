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
