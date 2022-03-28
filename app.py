from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, this code was updated locally and pushed to azure devops"

