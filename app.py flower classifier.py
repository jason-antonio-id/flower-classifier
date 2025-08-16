from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import numpy as np

# Initialize FastAPI
app = FastAPI(title="Iris Classifier API")

# Train Iris model at startup
iris = load_iris()
X, y = iris.data, iris.target
model = LogisticRegression(max_iter=200)
model.fit(X, y)
target_names = iris.target_names.tolist()

# Request body structure
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def root():
    return {"message": "Iris API is running. Go to /docs to test it."}

@app.post("/predict")
def predict(features: IrisFeatures):
    x = np.array([[features.sepal_length, features.sepal_width,
                   features.petal_length, features.petal_width]])
    idx = int(model.predict(x)[0])
    prob = float(model.predict_proba(x)[0][idx])
    return {"species": target_names[idx], "confidence": round(prob, 4)}

