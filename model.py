import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_curve, auc
import xgboost as xgb
import pickle

df = pd.read_csv("Pulsar.csv")

X = df.iloc[:,:-1]
Y = df.iloc[:,-1]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, stratify= Y, random_state = 45)

xgb_model = xgb.XGBClassifier(random_state=42)
xgb_model.fit(X_train, Y_train)


# Especifica el nombre del archivo en el que deseas guardar el modelo
archivo_modelo = "model.pkl"

# Guarda el modelo en el archivo
with open(archivo_modelo, 'wb') as archivo:
    pickle.dump(xgb_model, archivo)
