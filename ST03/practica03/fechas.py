#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import sys , os , shutil
import datetime , pytz , time
import types


def openfile (fileName , mode) :
    try :
        fich = open(fileName , mode)
        return fich
    except IOError :
        sys.stderr.write("Error open file " + fileName + " mode : " + mode.upper() + '\n')
        raise SystemExit

def isnumber (string) :
    try :
        int(string)
        return True
    except ValueError :
        sys.stderr.write("Error casting the field to integer " + string + '\n')
        return False

def islistNumb (list) :
    result = True

    for x in range(len(list)) :
        if not isnumber(list[x]) :
            result = False

    return result

def istimeStamp (list) :
    return islistNumb(list)


def isYear (year) :
    return int(year) > 1900 and int(year) < 2100

def isMonth (month) :
    return int(month) > 0 and int(month) < 13

def isDay (day) :
    return int(day) > 0 and int(day) < 32

def isdate (date) :
    return isYear(date[0]) and isMonth(date[1]) and isDay(date[2])

def isformatdate (dateformat) :
    date = []
    date = dateformat.split('-')

    if not (len(date) == 3 and islistNumb(date)) :
        return False

    return isdate(date)

def isAHour (hour) :
    return int(hour) >= 0 and int(hour) < 24

def isminute (minute) :
    return int(minute) >= 0 and int(minute) < 60

def issecond(second) :
    return int(second) >= 0 and int(second) < 60

def ishour (hour) :
    return isAHour(hour[0]) and isminute(hour[1]) and issecond(hour[2])

def isformathour (hourformat) :
    hour = []
    hour = hourformat.split(':')

    if len(hour) != 3 :
        return False

    if hour[2].find(',') :
        hour[2] = hour[2].replace(',' , '')

    if not islistNumb(hour) :
        return False

    return ishour(hour)

def isZone (string) :
    zones = ["Madrid", "Londres" , "Moscu" , "Tokio" , "New_York" , "UTC"]
    return string.strip() in zones

def isUTFformat (list) :
    return isnumber(list[0]) and isformatdate(list[1]) \
            and isformathour(list[2]) and isZone(list[3])

def getYear (date) :
    return int(date[0])

def getMonth(date) :
    return int(date[1])

def getDay (date) :
    return int(date[2])

def getHour (hour) :
    return int(hour[0])

def getMinute (hour) :
    return int(hour[1])

def getSecond (hour) :
    second = hour[2]
    if second.find(',') :
        second = second.replace(',' , '')
    return int(second)

def printnumLine (numline) :
    if int(numline) < 10 :
        print numline + '  ' ,
    elif int(numline) < 100 :
        print numline + ' ' ,
    else :
        print numline + '',


def getDateTime (dateformat , utc) :
    year = getYear(dateformat[1].split('-'))
    month = getMonth(dateformat[1].split('-'))
    day = getDay(dateformat[1].split('-'))
    hour = getHour(dateformat[2].split(':'))
    minute = getMinute(dateformat[2].split(':'))
    second = getSecond(dateformat[2].split(':'))

    dt = datetime.datetime(year , month , day , hour , minute , second , tzinfo=utc)

    return dt

def impUTCdf (numline , dateformat) :
    fmt = "%Y-%m-%d %H:%M:%S %Z%z"
    utc = pytz.utc
    dt  = getDateTime(dateformat , utc)

    printnumLine(numline)
    print dt.strftime(fmt)# 2016-03-05 19:47:53 UTC+0000


def impUTCts (numline , ts) :
    utc = pytz.utc
    fmt = "%Y-%m-%d %H:%M:%S %Z%z"

    # Convert Timestamp in datetime
    dt = datetime.datetime.fromtimestamp(ts)
    dt = utc.localize(dt)

    printnumLine(numline)
    print dt.strftime(fmt)

def imptsts (numline , ts) :

    printnumLine(numline)
    print ts

def imptsdt (numline , dateformat) :
    fmt = "%Y-%m-%d %H:%M:%S %Z%z"
    utc=pytz.utc
    ts=time.time()

    #Convert data time in Timestamp
    dt = getDateTime(dateformat , utc)
    ts = time.mktime(dt.timetuple())

    printnumLine(numline)
    print int(ts)

def impZonets (numline , ts) :
    fmt = "%Y-%m-%d %H:%M:%S %Z%z"
    utc=pytz.utc
    ts=time.time()

    printnumLine(numline)
    print int(ts)

def setTimezone (dt , zone) :
    zones = ["Madrid", "Londres" , "Moscu" , "Tokio" , "New_York" , "UTC"]
    zonesdt = []

    zonesdt.append(pytz.timezone("Etc/GMT+1"))
    zonesdt.append(pytz.timezone("Etc/GMT+0"))
    zonesdt.append(pytz.timezone("Etc/GMT+3"))
    zonesdt.append(pytz.timezone("Etc/GMT+9"))
    zonesdt.append(pytz.timezone("Etc/GMT-5"))
    zonesdt.append(pytz.timezone("Etc/GMT+1"))

    dt = dt.astimezone(zonesdt[zones.index(zone)])
    return dt

def getTimeZone (zone) :
    zones = ["Madrid", "Londres" , "Moscu" , "Tokio" , "New_York" , "UTC"]
    zonesdt = []

    zonesdt.append(pytz.timezone("Etc/GMT+1"))
    zonesdt.append(pytz.timezone("Etc/GMT+0"))
    zonesdt.append(pytz.timezone("Etc/GMT+3"))
    zonesdt.append(pytz.timezone("Etc/GMT+9"))
    zonesdt.append(pytz.timezone("Etc/GMT-5"))
    zonesdt.append(pytz.timezone("Etc/GMT+1"))

    return zonesdt[zones.index(zone)]

def impZonedf (numline , dateformat , zone , zonearg) :
    fmt = "%Y-%m-%d %H:%M:%S %Z%z"

    timezone = getTimeZone(zonearg)

    ts  = time.time()
    dt  = getDateTime(dateformat , timezone)
    dt = setTimezone(dt , zone)

    printnumLine(numline)
    print dt.strftime(fmt)


def procline (line) :
    linelist = []
    linelist = line.split(' ')

    if len(linelist) == 2 and istimeStamp(linelist) :

        #impUTCts(linelist[0] , int(linelist[1]))
        #imptsts(linelist[0] , linelist[1])
        impZonets(linelist[0] , linelist[1])

    elif len(linelist) == 4 and isUTFformat(linelist) :

        #impUTCdf(linelist[0] ,  linelist)
        impZonedf(linelist[0] , linelist , linelist[3]  , "Madrid")
        #imptsdt(linelist[0] , linelist)

    else :

        print "Bad format of time in line : " + line
        raise SystemExit


def readfile (filename) :
    fileR = openfile(filename , "r")
    data = []
    for x in fileR.readlines() :
        if x.strip() != '' :
            procline(x.strip())

def main () :
    readfile("ejemplotime.txt")

if __name__ == "__main__" :
    main()
