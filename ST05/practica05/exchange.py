#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import sys
import flask
import json
import requests
import os
import time

app = flask.Flask(__name__)

FAIL = "Amount must be a number to know the amount of bitcoins conversion..."

def openfile (fileName , mode) :
    try :

        fich = open(fileName , mode)
        return fich

    except IOError :

        sys.stderr.write("Error open file " + fileName + " mode : " + mode.upper() + '\n')
        raise SystemExit


def oldCache (name) :
    fiveMins = 300
    oneDay = 3600*24
    btcEx = "cny.json"

    cacheF = openfile(name , "r")
    cacheD = cacheF.read()
    cacheF.close()
    cacheJ = json.loads(cacheD)

    if btcEx in name :
        cacheTime = (time.time() - cacheJ["date"]) - fiveMins
    else :
        cacheTime = (time.time() - cacheJ["date"]) - oneDay

    return cacheTime > 0


def isCache (name) :
    return os.path.exists(name) and not oldCache(name)


def checkJson (data) :

    dataS = str(data)
    dataS = dataS.replace("'" , '"')
    dataS = dataS.replace("u\"" , "\"")

    return dataS


def getReq (url , name) :
    data  = {}

    try :
        if isCache(name) :
            # Get information exchange from local cache.
            print "Data get from cache..." + name
            cacheF = openfile(name , "r")
            cacheD = cacheF.read()
            data = json.loads(cacheD)

        else :

            print "Data get from server..." + name
            # Get information exchange from server...
            r = requests.get(url)
            if r.status_code == 200 :
                data = r.json()
            else :
                print "Error : " + str(r.status_code)

            # Update file with cache value in json format and actual time.
            data["date"] = time.time()
            dataS = checkJson(data)
            cache = openfile(name , "w+")
            cache.write(dataS)
            cache.close()

        return data

    except :

        sys.stderr.write("Error in request server or cache file...." + '\n')
        raise SystemExit

@app.route('/')
def index () :
    return "Hello World"


def isAmount (query_string) :
    keys = query_string.keys()
    return keys[0] == 'amount'

def isPars (query_string) :
    return len(query_string) == 1 and  isAmount(query_string)


def getCny () :
    """Get the value of bitcoins in chinense money to conversions...."""
    try :

        url = "https://data.btcchina.com/data/ticker?market=btccny"
        btcCny = getReq(url , "cny.json")
        return float(btcCny["ticker"]["buy"])

    except ValueError :
        print FAIL + "GET XBTCNT EXCHANGE"
        raise SystemExit


@app.route ('/exchange/XBTRUB')
def xbtRub () :
    """Change bitcoin to japanese money..."""
    query_string = flask.request.args

    try :

        btcCny = getCny()
        url = "http://api.fixer.io/latest?base=RUB"
        jsonExchanges = getReq(url , "rub.json")
        rubCny = jsonExchanges["rates"]["CNY"]
        btcRub = btcCny / rubCny

        if isPars(query_string) :
            btcRub *= float(query_string["amount"])

        return json.dumps(str(btcRub))

    except ValueError :
        return FAIL + "XBTRUB"


@app.route ('/exchange/XBTCHF')
def xbtChf () :
    """Change bitcoin to japanese money..."""
    query_string = flask.request.args

    try :

        btcCny = getCny()
        url = "http://api.fixer.io/latest?base=CHF"
        jsonExchanges = getReq(url , "chf.json")
        chfCny = jsonExchanges["rates"]["CNY"]
        btcChf = btcCny / chfCny

        if isPars(query_string) :
            btcChf *= float(query_string["amount"])

        return json.dumps(str(btcChf))

    except ValueError :
        return FAIL + "XBTCHF"


@app.route ('/exchange/XBTAUD')
def xbtAud () :
    """Change bitcoin to japanese money..."""
    query_string = flask.request.args

    try :

        btcCny = getCny()
        url = "http://api.fixer.io/latest?base=AUD"
        jsonExchanges = getReq(url , "aud.json")
        audCny = jsonExchanges["rates"]["CNY"]
        btcAud = btcCny / audCny

        if isPars(query_string) :
            btcAud *= float(query_string["amount"])

        return json.dumps(str(btcAud))

    except ValueError :
        return FAIL + "XBTAUD"


@app.route ('/exchange/XBTJPY')
def xbtJpy () :
    """Change bitcoin to japanese money..."""
    query_string = flask.request.args

    try :

        btcCny = getCny()
        url = "http://api.fixer.io/latest?base=JPY"
        jsonExchanges = getReq(url , "jpy.json")
        jpyCny = jsonExchanges["rates"]["CNY"]
        btcJpy = btcCny / jpyCny

        if isPars(query_string) :
            btcJpy *= float(query_string["amount"])

        return json.dumps(str(btcJpy))

    except ValueError :
        return FAIL + "XBTJPY"


@app.route ('/exchange/XBTCAD')
def xbtCad () :
    """Change bitcoin to canadiense dollar..."""
    query_string = flask.request.args

    try :

        btcCny = getCny()
        url = "http://api.fixer.io/latest?base=CAD"
        jsonChanges = getReq(url , "cad.json")
        cnyCad = jsonChanges["rates"]["CNY"]
        cadBtc = btcCny / cnyCad

        if isPars(query_string) :

            cadBtc *= float(query_string["amount"])
        return json.dumps(str(cadBtc))

    except ValueError :
        return FAIL + "XBTCAD"

@app.route ('/exchange/XBTUSD')
def xbtUsd () :
    """Get the value of bitcoins in dollars..."""
    query_string= flask.request.args

    try :

        btcCny = getCny()
        url = "http://api.fixer.io/latest?base=USD"
        jsonExchanges = getReq(url , "usd.json")
        cnyUsd = jsonExchanges["rates"]["CNY"]
        usdBtc = btcCny / cnyUsd

        if isPars(query_string) :
            usdBtc *= float(query_string["amount"])

        return json.dumps(str(usdBtc))

    except ValueError:
        return FAIL + "XBTUSD"


@app.route ('/exchange/XBTGBP')
def xbtGbp () :
    query_string = flask.request.args

    try :

        btcCny = getCny()

        url = "http://api.fixer.io/latest?base=GBP"
        jsonExchanges = getReq(url , "gbp.json")

        cnyGbp = jsonExchanges["rates"]["CNY"]
        btcGbp = btcCny / cnyGbp

        if isPars(query_string) :
            btcGbp *= float(query_string["amount"])

        return json.dumps(str(btcGbp))

    except ValueError :

        return FAIL + "XBTGBP"


@app.route ('/exchange/XBTEUR')
def xbtEur () :
    """Obtain the value of bitcoin in EUR"""
    query_string = flask.request.args

    try :

        btcCny = getCny()
        url = "http://api.fixer.io/latest?base=EUR"
        jsonExchanges = getReq(url , "eur.json")
        cnyEur = jsonExchanges["rates"]["CNY"]

        btcEur = btcCny / cnyEur

        if isPars(query_string) :
            btcEur *= float (query_string["amount"])

        return json.dumps(str(btcEur))

    except ValueError :
        return FAIL + "XBTEUR"


@app.route('/exchange/XBTCNY')
def xbtCny () :
    """Obtain the value of bintcoin in chinense value"""
    query_string = flask.request.args

    try :

        btcCny = getCny()
        if isPars (query_string) :
            btcCny *= float(query_string["amount"])

        return json.dumps(str(btcCny))

    except ValueError :
        return FAIL + "XBTCNY"

if __name__ == "__main__" :
    app.run(debug=True)
