🌸 Iris Flower Classifier API

A simple FastAPI project that uses a Machine Learning model to classify Iris flowers into one of three species:

Setosa

Versicolor

Virginica

The classification is based on sepal length, sepal width, petal length, and petal width.

🚀 Features

REST API built with FastAPI

Predict Iris flower species from input features

Interactive API docs with Swagger UI (/docs)

Returns prediction and confidence score

📂 Project Structure
iris-api/
│-- app.py            # FastAPI app (endpoints)
│-- main.py           # Entry point to run the API
│-- model.pkl         # Trained machine learning model (scikit-learn)
│-- requirements.txt  # Dependencies
│-- README.md         # Project documentation
│-- .venv/            # Virtual environment (not pushed to repo)

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/iris-api.git
cd iris-api

2️⃣ Create a virtual environment
python -m venv .venv

3️⃣ Activate the virtual environment

Windows (PowerShell):

.venv\Scripts\activate


Mac/Linux:

source .venv/bin/activate

4️⃣ Install dependencies
pip install -r requirements.txt

▶️ Running the API
Option 1: Run with Uvicorn
uvicorn app:app --reload

Option 2: Run with main.py
python main.py

🌐 API Endpoints
🔹 Root

GET /

{
  "message": "Hello from FastAPI!"
}

🔹 Predict Flower Species

POST /predict

Example request:
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}

Example response:
{
  "prediction": "setosa",
  "confidence": 0.98
}

📊 Model Info

Trained on the Iris dataset (scikit-learn)

Supports 3 flower species:

setosa

versicolor

virginica

🛠️ Tech Stack

Python

FastAPI

Scikit-learn

Uvicorn

📖 How to Use

Start the server with:

uvicorn app:app --reload


Open your browser at 👉 http://127.0.0.1:8000/docs

Use Swagger UI to test the /predict endpoint with your own flower measurements

✅ Example Use Cases

Test different flower inputs and see predicted species

Integrate with a frontend chatbot later for interactive predictions

Extend with more datasets or flower types

👨‍💻 Author

Made with ❤️ by Your Name
