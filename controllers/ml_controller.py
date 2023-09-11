from fastapi import APIRouter, HTTPException, status
from models import Prediction_Input, Prediction_Output

import pandas as pd
import numpy as np
import xgboost as xgb
import pickle

router = APIRouter()

# Especifica el nombre del archivo en el que deseas guardar el modelo
archivo_modelo = "model.pkl"

# Guarda el modelo en el archivo
with open(archivo_modelo, 'rb') as archivo:
    xgb_model = pickle.load(archivo)


preds = []

@router.get("/ml")
def get_preds():
    return preds



@router.post("/ml", status_code= status.HTTP_201_CREATED)
def predict(pred_input: Prediction_Input):
    prediction = xgb_model.predict(pred_input)
    prediction_dict = {"id": str(pred_input.id), "input":(pred_input.input), "pred":prediction}
    preds.append(pred_input)
    return prediction_dict
