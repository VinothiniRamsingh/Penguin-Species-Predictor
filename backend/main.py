from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

app = FastAPI()

# Train once at startup
df = pd.read_csv(
    "https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv"
)

X = pd.get_dummies(df.drop("species", axis=1))
y = df["species"]

model = RandomForestClassifier()
model.fit(X, y)

class Penguin(BaseModel):
    island: str
    sex: str
    bill_length_mm: float
    bill_depth_mm: float
    flipper_length_mm: float
    body_mass_g: float

@app.post("/predict")
def predict(penguin: Penguin):
    input_df = pd.DataFrame([penguin.dict()])
    input_df = pd.get_dummies(input_df)
    input_df = input_df.reindex(columns=X.columns, fill_value=0)

    pred = model.predict(input_df)[0]
    probs = model.predict_proba(input_df)[0]

    return {
        "species": pred,
        "probabilities": {
            "Adelie": float(probs[0]),
            "Chinstrap": float(probs[1]),
            "Gentoo": float(probs[2])
        }
    }
