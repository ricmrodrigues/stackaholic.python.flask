from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.get("/")
def read_root():
    return jsonify(
        Hello="World"
    )