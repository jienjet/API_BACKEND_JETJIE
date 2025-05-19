from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow all origins by default

@app.route('/')
def hello():
    return "Hello from Flask!"
