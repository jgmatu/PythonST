#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import sys , os , shutil
import calendar, datetime , pytz , time
import types
from argparse import ArgumentParser
import json


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
    zones = ["madrid", "londres" , "moscu" , "tokio" , "new_york" , "utc"]
    return string.strip().lower() in zones

def isUTFformat (list) :
    return isnumber(list[0]) and isformatdate(list[1]) and \
                isformathour(list[2]) and isZone(list[3])

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
        # The last field has a , we have to remove this character of seconds
        # field.
        second = second.replace(',' , '')

    return int(second)

def printnumLine (numline) :
    """Format field numline in output."""
    if int(numline) < 10 :
        print numline + '  ' ,
    elif int(numline) < 100 :
        print numline + ' ' ,
    else :
        print numline + '',


def getDateTime (dateformat) :

    year = getYear(dateformat[1].split('-'))
    month = getMonth(dateformat[1].split('-'))
    day = getDay(dateformat[1].split('-'))

    hour = getHour(dateformat[2].split(':'))
    minute = getMinute(dateformat[2].split(':'))
    second = getSecond(dateformat[2].split(':'))

    dt = datetime.datetime(year , month , day , hour , minute , second)
    return dt

def getTimeZone (zone) :
    zones = ["madrid", "londres" , "moscu" , "tokio" , "new_york" , "utc"]
    zonesdt = []

    zonesdt.append(pytz.timezone("Europe/Madrid"))
    zonesdt.append(pytz.timezone("Europe/London"))
    zonesdt.append(pytz.timezone("Europe/Moscow"))
    zonesdt.append(pytz.timezone("Asia/Tokyo"))
    zonesdt.append(pytz.timezone("America/New_York"))
    zonesdt.append(pytz.timezone("UTC"))

    return zonesdt[zones.index(zone.lower())]

def impUTCdf (numline , dateformat , zone , jsonarg) :
    fmt = "%Y-%m-%d %H:%M:%S %Z %z"
    utc = pytz.utc

    dt = getDateTime(dateformat)
    zonetime = getTimeZone(zone.lower())

    dt = zonetime.localize(dt)
    dt = dt.astimezone(utc)

    if not jsonarg :
        # Print default format of hour.
        printnumLine(numline)
        print dt.strftime(fmt)
    else :
        # Print in json format the hour.
        print json.dumps({numline:str(dt)} , sort_keys=True , indent=4)

def impUTCts (numline , ts , jsonarg) :
    fmt = "%Y-%m-%d %H:%M:%S %Z %z"
    utc = pytz.utc

    # Convert Timestamp in datetime
    dt = datetime.datetime.fromtimestamp(ts)
    dt = utc.localize(dt)

    if not jsonarg :
        # Print default format the hour.
        printnumLine(numline)
        print dt.strftime(fmt)
    else :
        # Print json format the hour.
        print json.dumps({numline:str(dt)} , sort_keys=True , indent=4)


def imptsts (numline , ts , jsonarg) :
    """Directly the format"""

    if not jsonarg :
        # Default format
        printnumLine(numline)
        print ts
    else :
        # Json format.
        print json.dumps({numline:int(ts)} , sort_keys=True , indent=4)


def impdtts (numline , dateformat , zone , jsonarg) :
    fmt = "%Y-%m-%d %H:%M:%S  %z"
    utc = pytz.utc

    #Process zone in datetime format
    dt = getDateTime(dateformat) #Naive

    timezone = getTimeZone(zone.lower())
    dt = timezone.localize(dt) # zone

    dt = dt.astimezone(utc) #utc

    ts = calendar.timegm(dt.utctimetuple())

    if not jsonarg :
        # Print datetime format Timestamp.
        printnumLine(numline)
        print ts
    else :
        # Print datetime in json format.
        print json.dumps({numline:ts} , sort_keys=True , indent=4)


def impZonets (numline , ts , zonearg , jsonarg) :
    fmt = "%Y-%m-%d %H:%M:%S  %z"
    utc = pytz.utc

    # Time Stamp to datetime.
    dt = datetime.datetime.fromtimestamp(int(ts))
    dt = utc.localize(dt)

    #Get Conversion from Timestamp to zone.
    dt.astimezone(getTimeZone(zonearg))

    if not jsonarg :
        # Print default format.
        printnumLine(numline)
        print dt.strftime(fmt)
    else :
        #Print json format.
        print json.dumps({numline:str(dt)} , sort_keys=True , indent=4)


def impZonedf (numline , dateformat , zone , zonearg , jsonarg) :
    fmt = "%Y-%m-%d %H:%M:%S  %z"

    # Naive
    dt = getDateTime(dateformat)

    # Local Zone.
    timezone = getTimeZone(zone.lower())
    dt = timezone.localize(dt)

    # Get Conversion Zone.
    dt = dt.astimezone(getTimeZone(zonearg.lower()))

    if not jsonarg :
        #Print default format.
        printnumLine(numline)
        print dt.strftime(fmt)
    else :
        #Print json format.
        print json.dumps({numline:str(dt)} , sort_keys=True , indent=4)

def isEquals (mode , argzone) :
    equals = True;

    if (len(mode) != len(argzone)) :
        # If not are equals length finish they are not the same word.
        equals = False

    pos = 0;
    while (pos < len(mode) and equals) :
        # Check the character of words to check if are equals.
        if (argzone[pos] == mode[pos]) :
            pos = pos + 1
        else :
            equals = False
    return equals



def modeUTC (argzone) :
    return argzone == None or isEquals("utc" , argzone)

def modeTs (argzone) :
    return argzone != None and isEquals("epoch" , argzone)

def modeZone (argzone) :
    return argzone != None and isZone(argzone)

def isArgZone (argzone) :
    return argzone != None and isZone(argzone)

def procline (line , args) :
    linelist = []
    linelist = line.split(' ')

    if len(linelist) == 2 and istimeStamp(linelist) :
        # The line is in format date to get the datetime conversion necessary.

        if modeUTC(args.argzone) :
            # Get the time in UTC.
            impUTCts(linelist[0] , int(linelist[1]) , args.json)

        if modeTs(args.argzone) :
            # Get the time in Timestamp
            imptsts(linelist[0] , linelist[1] , args.json)

        if isArgZone(args.argzone) and not modeUTC(args.argzone) :
            # Get the time in Zone of args.
            impZonets(linelist[0] , linelist[1] , args.argzone , args.json)

    elif len(linelist) == 4 and isUTFformat(linelist) :
        # The line is in format Timestamp to get the datetime conversion
        # necesary

        if modeUTC(args.argzone) :
            # Get the time in UTC.
            impUTCdf(linelist[0] ,  linelist , linelist[3] , args.json)

        if modeTs (args.argzone) :
            # Get the time in Timestamp.
            impdtts(linelist[0] , linelist , linelist[3] , args.json)

        if isArgZone(args.argzone) and not modeUTC(args.argzone):
            # Get the time in Zone of args.
            impZonedf(linelist[0] , linelist, linelist[3] ,  args.argzone , args.json)

    else :

        # Is not a valid format the script must die.
        sys.stderr.write("Bad format of time in line : " + line + '\n')
        raise SystemExit


def readfile (args) :
    data = []
    for x in sys.stdin.readlines() :
        # Read line by line the file and get the conversion of datetimes and
        # zones.
        if x.strip() != '' :
            procline(x.strip() , args)

def main () :
    usage = "Uso %prog [opciones]"
    parser = ArgumentParser(usage)

    parser.add_argument("-t" , "--timezone" , action="store" , dest="argzone" ,\
                            help="Zone to proc the time")

    parser.add_argument("-j" , "--json" , dest="json" , action="store_true" , \
                            help="Output in json format")

    args = parser.parse_args()
    readfile(args)

if __name__ == "__main__" :
    main()
