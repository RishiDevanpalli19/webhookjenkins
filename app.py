# This is a simple flask app that displays "Hello World"

from flask import Flask

app = Flask(_name_)

@app.route("/")

def hello():
    return "<h2>Hello world - Integration Activity Flask Deployment Lab<h2><hr/>"\


app.run(host="0.0.0.0", port=5000)
