from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

class Transaction(BaseModel):
    Amount: float
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float

@app.post("/predict/")
async def predict(transaction: Transaction):
    # Implémentation de la logique de prédiction
    
    if transaction.Amount > 1000:
        return {"prediction": "fraudulent"}
    else:
        return {"prediction": "not fraudulent"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

