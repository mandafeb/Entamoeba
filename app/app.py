from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import desc_calc
from app.model.model import __version__ as model_version
import uvicorn 

app = FastAPI()

class api_data(BaseModel):
    mol : str
    che : int

# class PredictionOut(BaseModel):
#     pic: str 

@app.route('/')
@app.route('/app')

@app.get('/')
def home():
    return{'health_check': 'OK', 'model_version': model_version}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

@app.post('/predict/')
def predict(payload: api_data):
    model = desc_calc(payload.mol)
    return model['pIC50']

# if __name__ == "__main__":
#     uvicorn.run("api:app", host = "0.0.0.0", port = 8000)