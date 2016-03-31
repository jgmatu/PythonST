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

    dt = datetime.datetime(2013 , 6 , 19 , 15 , 9 , 25)
    return dt


def impdtts (numline , dateformat , zone , jsonarg) :
    fmt = "%Y-%m-%d %H:%M:%S  %z"
    utc = pytz.utc

    #Process zone in datetime format
    dt = getDateTime(dateformat) #Naive

    timezone = getTimeZone(zone.lower())
    dt = timezone.localize(dt) # zone
    dt = dt.astimezone(utc) #utc

    print dt

    ts = matplotlib.dates.date2num(dt)
    ts = matplotlib.dates.num2epoch(ts)



    if not jsonarg :
        # Print datetime format Timestamp.
        printnumLine(numline)
        print int(ts)
    else :
        # Print datetime in json format.
        print json.dumps({numline:ts} , sort_keys=True , indent=4)

def main () :
    impdtts(str(1) , None , "Madrid" , False)


if __name__ == "__main__" :
    main()
