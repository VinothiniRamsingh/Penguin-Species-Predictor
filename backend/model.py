import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Train model once
df = pd.read_csv(
    "https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv"
)

X = df.drop("species", axis=1)
y = df["species"]

X = pd.get_dummies(X)
y_map = {"Adelie": 0, "Chinstrap": 1, "Gentoo": 2}
y = y.map(y_map)

model = RandomForestClassifier()
model.fit(X, y)

def predict(data: dict):
    input_df = pd.DataFrame([data])
    input_df = pd.get_dummies(input_df)
    input_df = input_df.reindex(columns=X.columns, fill_value=0)

    pred = model.predict(input_df)[0]
    return list(y_map.keys())[pred]
