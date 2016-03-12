#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import sys , os , shutil
import pytz , time , datetime


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

    print str(zonesdt[zones.index(zone)]) + " " + zone.upper()
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


def imptsdt (numline , dateformat , zone) :
    fmt = "%Y-%m-%d %H:%M:%S  %z"
    utc = pytz.utc
    ts = time.time()

    #Convert data time in Timestamp
    dt = getDateTime(dateformat)
    timezone = getTimeZone(zone.lower())

    dt = timezone.localize(dt)

    dt = dt.astimezone(utc)

    ts = time.mktime(dt.timetuple())

    if zone.strip() is "Madrid" :
        ts += time.timezone

    printnumLine(numline)
    print int(ts)


def main () :
    imptsdt(str(1) , None , "Madrid")


if __name__ == "__main__" :
    main()
