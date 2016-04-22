#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import sys
import flask
import json
import requests

app = flask.Flask(__name__)


def getReq (url) :
    data = {}

    r = requests.get(url)
    if r.status_code == 200 :
        data = r.json()
    else :
        print "Error : " + str(r.status_code)

    return data


@app.route('/')
def index () :
    return "Hello World"


def isAmount (query_string) :
    keys = query_string.keys()
    return keys[0] == 'amount'

def isPars (query_string) :
    return len(query_string) == 1 and  isAmount(query_string)



def getCny () :

    try :

        url = "https://data.btcchina.com/data/ticker?market=btccny"
        btcCny = getReq(url)
        return float(btcCny["ticker"]["buy"])

    except :

        return None

@app.route ('/exchange/XBTGBP')
def xbtGbp () :
    query_string = flask.request.args
    


@app.route ('/exchange/XBTEUR')
def xbtEur () :
    query_string = flask.request.args


    try :
        valBtcCny = getCny()
        url = "http://api.fixer.io/latest?base=EUR"
        cnyeur = getReq(url)
        valCnyEur = cnyeur["rates"]["CNY"]

        resJson = valBtcCny / valCnyEur

        if isPars(query_string) :
            resJson = resJson * float (query_string["amount"])

        return json.dumps(str(resJson))

    except :

        return "Amount must be a number to know the amount of bitcoinss conversion..."


@app.route('/exchange/XBTCNY')
def xbtCny () :
    query_string = flask.request.args

    try :

        valCny = getCny()
        if isPars (query_string) :
            valCny = valCny * float(query_string["amount"])

        return json.dumps(str(valCny))

    except :

        return "Amount must be a number to know the amount of bitcoinss conversion..."

if __name__ == "__main__" :
    app.run(debug=True)
