# This is a simple flask app that displays "Hello World"

from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello():
    return "<h2>Hello world - Integration Activity Flask Deployment Lab: try 2 <h2><hr/>"\


app.run(host="0.0.0.0", port=5000)
