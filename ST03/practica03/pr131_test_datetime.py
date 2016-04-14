#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import time , datetime , pytz , calendar

madrid=pytz.timezone("Europe/Madrid")
londres=pytz.timezone("Europe/London")
moscu=pytz.timezone("Europe/Moscow")
tokio=pytz.timezone("Asia/Tokyo")
new_york=pytz.timezone("America/New_York")
utc = pytz.utc

def compara(original , current):
    if original == current:
        print "ok"
    else:
         print "fail"
    return

def main():
    ts = int(time.time())
    original = ts
    dt = datetime.datetime.fromtimestamp(ts)

    dt=madrid.localize(dt)
    ts = calendar.timegm(dt.utctimetuple())
    compara(original , ts)  # iguales

    dt = utc.normalize(dt.astimezone(utc))
    ts = calendar.timegm(dt.utctimetuple())
    compara(original,ts)  # iguales

    dt = dt.astimezone(moscu)
    ts = calendar.timegm(dt.utctimetuple())
    compara(original,ts)  # iguales

    dt = dt.astimezone(tokio)
    ts = calendar.timegm(dt.utctimetuple())
    compara(original,ts)  # iguales

    return

if __name__ == "__main__":
    main()
