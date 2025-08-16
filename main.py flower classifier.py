import requests

API_URL = "http://127.0.0.1:8000/predict"  # must match the endpoint in app.py

def test_prediction():
    sample = {
        "sepal_length": 9.9,
        "sepal_width": 9.9,
        "petal_length": 9.9,
        "petal_width": 9.9
    }

    response = requests.post(API_URL, json=sample)
    if response.status_code == 200:
        print("✅ Prediction:", response.json())
    else:
        print("❌ Error:", response.text)

if __name__ == "__main__":
    test_prediction()





        
    