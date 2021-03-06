#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import sys , os , shutil
import calendar, datetime , pytz , time
import types
from argparse import ArgumentParser
from matplotlib import dates
import json
import xml.etree.cElementTree as ET
import xmlpp


MAXTS = 14

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

def impUTCdf (numline , dateformat , zone , args , listJson , root) :
    fmt = "%Y-%m-%d %H:%M:%S \t %Z %z"
    utc = pytz.utc
    atributos = {}

    dt = getDateTime(dateformat)
    zonetime = getTimeZone(zone.lower())

    dt = zonetime.localize(dt)
    dt = dt.astimezone(utc)

    if args.json :

        #Get Object Json to Array.
        listJson.append({numline:str(dt)})

    elif args.ascii :

        # Print default format of hour.
        printnumLine(numline)
        print dt.strftime(fmt)

    else :

        elemento = ET.SubElement(root , u"instant")
        atributos["date"]    = dt.strftime(fmt)
        atributos["ordinal"] = numline
        elemento.attrib      = atributos


def impUTCts (numline , ts , args , listJson , root) :
    fmt = "%Y-%m-%d %H:%M:%S \t %Z %z"
    utc = pytz.utc
    atributos = {}

    # Convert Timestamp in datetime
    dt = datetime.datetime.utcfromtimestamp(ts)
    dt = utc.localize(dt)

    if args.json :

        # Get Object Json to Array.
        listJson.append({numline:str(dt)})

    elif args.ascii :

        # Print default format the hour.
        printnumLine(numline)
        print dt.strftime(fmt)

    else :

        elemento = ET.SubElement(root , u"instant")
        atributos["date"]    = dt.strftime(fmt)
        atributos["ordinal"] = numline
        elemento.attrib      = atributos


def imptsts (numline , ts , args , listJson , root) :
    """Directly the format"""
    atributos = {}

    if args.json :

        #Get Object Json to Array.
        listJson.append({numline:int(ts)})

    elif args.ascii :

        # Default format
        printnumLine(numline)
        print ts

    else :

        whites = MAXTS - len(unicode(ts))
        elemento = ET.SubElement(root , u"instant")
        atributos["date"]    = unicode(ts) +  whites* ' '
        atributos["ordinal"] = numline
        elemento.attrib      = atributos


def impdtts (numline , dateformat , zone , args , listJson , root) :
    fmt = "%Y-%m-%d %H:%M:%S  %z"
    utc = pytz.utc
    atributos = {}

    #Process zone in datetime format
    dt = getDateTime(dateformat) #Naive

    timezone = getTimeZone(zone.lower())
    dt = timezone.localize(dt) # zone
    dt = dt.astimezone(utc) #utc

    ts = time.mktime(dt.utctimetuple())

    if args.json :

        # Get Object Json to Array.
        listJson.append({numline:ts})

    elif args.ascii :

        # Print datetime format Timestamp.
        printnumLine(numline)
        print int(ts)

    else :

        whites = MAXTS - len(unicode(ts))
        elemento = ET.SubElement(root , u"instant")
        atributos["date"]    = unicode(ts) + whites * ' '
        atributos["ordinal"] = numline
        elemento.attrib      = atributos



def impZonets (numline , ts , args , listJson , root) :
    fmt = "%Y-%m-%d %H:%M:%S \t %z"
    timezone = getTimeZone(args.zone)
    utc = pytz.utc
    atributos = {}

    # Time Stamp to datetime.
    dt = datetime.datetime.utcfromtimestamp(int(ts))
    dt = utc.localize(dt)

    dt = dt.astimezone(timezone)

    if args.json :

        # Get Object Json to Array.
        listJson.append({numline:str(dt)})

    elif args.ascii :

        # Print default format.
        printnumLine(numline)
        print dt.strftime(fmt)

    else :

        elemento = ET.SubElement(root , u"instant")
        atributos["date"]    = dt.strftime(fmt)
        atributos["ordinal"] = numline
        elemento.attrib      = atributos


def impZonedf (numline , dateformat , zone , args , listJson , root) :
    fmt = "%Y-%m-%d %H:%M:%S \t %z"
    atributos = {}

    # Naive
    dt = getDateTime(dateformat)

    # Local Zone.
    timezone = getTimeZone(zone.lower())
    dt = timezone.localize(dt)

    # Get Conversion Zone.
    dt = dt.astimezone(getTimeZone(args.zone))

    if args.json :

        # Get Object Json to Array.
        listJson.append({numline:str(dt)})

    elif args.ascii :

        #Print default format.
        printnumLine(numline)
        print dt.strftime(fmt)

    else :

        elemento = ET.SubElement(root , u"instant")
        atributos["date"]    = dt.strftime(fmt)
        atributos["ordinal"] = numline
        elemento.attrib      = atributos


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

def isXML (args) :
    return not args.ascii and not args.json

def isFirstLineXML (args , numline) :
    return isXML(args) and numline == "1"

def isTs (linelist) :
    return len(linelist) == 2 and istimeStamp(linelist)

def isDf (linelist) :
    return len(linelist) == 4 and isUTFformat(linelist)


def isXmlUtc (linelist , args) :
    return (isTs(linelist) or isDf(linelist)) and modeUTC(args.zone) and \
                isFirstLineXML(args , linelist[0])


def isXmlTs (linelist , args) :
    return (isTs(linelist) or isDf(linelist)) and modeTs(args.zone) and \
                isFirstLineXML(args , linelist[0])


def isXmlZone (linelist , args) :
    return (isTs(linelist) or isDf(linelist)) and isArgZone(args.zone) and  \
                not modeUTC(args.zone) and  isFirstLineXML(args , linelist[0])


def tsutc (args , linelist , listJson , root) :
    if modeUTC(args.zone) :
        # Get the time in UTC.
        impUTCts(linelist[0] , int(linelist[1]) , args , listJson , root)

def utcdf (args , linelist  , listJson  , root) :

    if modeUTC(args.zone) :
        # Get the time in UTC.
        impUTCdf(linelist[0] ,  linelist , linelist[3] , args , listJson , root)


def tsts (args , linelist , listJson , root) :
    if modeTs(args.zone) :
        # Get the time in Timestamp
        imptsts(linelist[0] , linelist[1] , args , listJson , root)


def dfts (args , linelist , listJson , root) :
    if modeTs (args.zone) :
        # Get the time in Timestamp.
        impdtts(linelist[0] , linelist , linelist[3] , args , listJson , root)

def tszone (args , linelist , listJson , root) :

    if isArgZone(args.zone) and not modeUTC(args.zone) :
        # Get the time in Zone of args.
        impZonets(linelist[0] , linelist[1] , args , listJson , root)

def dfzone (args , linelist , listJson , root) :

    if isArgZone(args.zone) and not modeUTC(args.zone):
        # Get the time in Zone of args.
        impZonedf(linelist[0] , linelist, linelist[3] , args , listJson , root)


def procline (line , args , listJson , root) :
    linelist = []
    attrib = {}

    linelist = line.split(' ')

    if isXmlUtc(linelist , args) :
        root.attrib = {u"city" : u"UTF"}

    if isXmlTs (linelist , args) :
        root.attrib = {u"city" : u"timestamp"}

    if isXmlZone(linelist , args) :
        root.attrib = {u"city" : unicode(args.zone)}


    if isTs (linelist) :
        # The line is in format date to get the datetime conversion necessary.
        tsutc (args , linelist , listJson , root)
        tsts(args , linelist ,  listJson , root)
        tszone(args , linelist , listJson , root)


    elif  isDf(linelist) :
        # The line is in format Timestamp to get the datetime conversion
        # necesary.
        utcdf (args , linelist  , listJson , root)
        dfts(args , linelist , listJson , root)
        dfzone(args , linelist , listJson , root)

    else :

        # Is not a valid format the script must die.
        sys.stderr.write("Bad format of time in line : " + line + '\n')
        raise SystemExit


def readfile (args) :
    listJson = []
    data = []

    root = ET.Element(u"instants")

    for x in sys.stdin.readlines() :
        # Read line by line the file and get the conversion of datetimes and
        # zones.
        if x.strip() != '' :
            procline(x.strip() , args , listJson , root)

    if args.json :
        print json.dumps(listJson , sort_keys = True , indent = 4)

    if isXML(args) :
        # Print XML Format.
        xmlData = ET.tostring(root , encoding="utf-8" , method="xml")
        xmlpp.pprint(xmlData , sys.stdout , 4 , 80)


def main () :
    usage = "Uso %prog [opciones]"
    parser = ArgumentParser(usage)

    parser.add_argument("-t" , "--timezone" , action="store" , dest="zone" ,    \
                            help="Zone to proc the time")

    parser.add_argument("-j" , "--json" , dest="json" , action="store_true" ,   \
                            help="Output in json format")

    parser.add_argument("-a" , "--ascii" , dest="ascii" , action="store_true" , \
                            help="Ascii mode")

    args = parser.parse_args()
    readfile(args)

if __name__ == "__main__" :
    main()
