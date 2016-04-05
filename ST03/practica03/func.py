#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import sys , os , shutil
import pytz , time , datetime
import calendar
import matplotlib
from matplotlib import dates

def printnumLine (numline) :
    if int(numline) < 10 :
        print numline + '  ' ,
    elif int(numline) < 100 :
        print numline + ' ' ,
    else :
        print numline + '',


def getTimeZone (zone) :
    zones = ["madrid", "londres" , "moscu" , "tokio" , "new_york" , "utc"]
    zonesdt = []

    zonesdt.append(pytz.timezone("Europe/Madrid"))
    zonesdt.append(pytz.timezone("Europe/London"))
    zonesdt.append(pytz.timezone("Europe/Moscow"))
    zonesdt.append(pytz.timezone("Asia/Tokyo"))
    zonesdt.append(pytz.timezone("America/New_York"))
    zonesdt.append(pytz.timezone("UTC"))

    return zonesdt[zones.index(zone)]

def getDateTime (dateformat) :
#    year = getYear(dateformat[1].split('-'))
#    month = getMonth(dateformat[1].split('-'))
#    day = getDay(dateformat[1].split('-'))
#    hour = getHour(dateformat[2].split(':'))
#    minute = getMinute(dateformat[2].split(':'))
#    second = getSecond(dateformat[2].split(':'))

    dt = datetime.datetime(2002 , 5 , 21 , 15 , 16 , 1)
    return dt


def impUTCts (numline , ts , jsonarg) :
    fmt = "%Y-%m-%d %H:%M:%S %Z %z"
    utc = pytz.utc

    # Convert Timestamp in datetime
    dt = datetime.datetime.utcfromtimestamp(ts)
    dt = utc.localize(dt)

    if not jsonarg :
        # Print default format the hour.
        printnumLine(numline)
        print dt.strftime(fmt)
    else :
        # Print json format the hour.
        print json.dumps({numline:str(dt)} , sort_keys=True , indent=4)



def main () :
    impUTCts("1"  , 1436762748 , False)


if __name__ == "__main__" :
    main()
