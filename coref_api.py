import logging 

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import spacy
import coreferee

logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)

# Load the spaCy model and add coreferee component
try:
    nlp = spacy.load("en_core_web_lg")
    nlp.add_pipe("coreferee")
except OSError:
    raise RuntimeError("Model 'en_core_web_lg' not found. Install it with 'python -m spacy download en_core_web_lg'")

# Initialize FastAPI
app = FastAPI()

# Request model
class TextRequest(BaseModel):
    text: str

@app.post("/resolve_coref")
def resolve_coreference(request: TextRequest):
    try:
        logger.info(f">>> {request.text}")
        doc = nlp(request.text)
        coref_list = []
        if doc._.coref_chains:
            for chain in doc._.coref_chains:
                coref_group = {str(token_id): doc[token_id].text for coref in chain for token_id in coref}
                coref_list.append(coref_group)
        return {"coreference_mapping": coref_list}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run with: uvicorn filename:app --reload
