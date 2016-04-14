#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


import flask
import json

POST = []
app = flask.Flask(__name__)

@app.route('/')
def index () :
    return "Hello World"

@app.route('/posts')
def post () :
    data = []

    data = json.loads(POST)

    return data



if __name__ == "__main__" :
    app.run(debug=True)
