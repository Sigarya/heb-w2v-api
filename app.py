import os
from gensim.models import KeyedVectors
from fastapi import FastAPI
from pydantic import BaseModel

# Load the model
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model.mdl')
model = KeyedVectors.load(MODEL_PATH)

app = FastAPI()

# Request body model
class SimilarityRequest(BaseModel):
    word1: str
    word2: str

@app.post("/similarity")
def get_similarity(request: SimilarityRequest):
    try:
        similarity = model.similarity(request.word1, request.word2)
        return {
            "word1": request.word1,
            "word2": request.word2,
            "similarity": similarity
        }
    except KeyError:
        return {
            "error": "One or both words not in vocabulary."
        }
