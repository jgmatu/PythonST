#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
# Miguel, march 2016

#         1         2         3         4         5         6         7         8
#123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890

import pytz , random , time , datetime
import calendar

madrid  = pytz.timezone("Europe/Madrid")
londres = pytz.timezone("Europe/London")
moscu = pytz.timezone("Europe/Moscow")
tokio = pytz.timezone("Asia/Tokyo")
new_york = pytz.timezone("America/New_York")
utc = pytz.utc
fmt = "%Y-%m-%d %H:%M:%S"
maxtime = time.time()
t0 = 946684800  # 2000.01.01
TIMES = 40

def random_date():
    ts = t0 + int(random.random() * (maxtime - t0))
    return ts

def add_city(ts):
    """Gets a timestamp , returns a tuple of 2 elements adding the
       same date specified as yyyy mm dd hh mm city"""

    dt = datetime.datetime.fromtimestamp(ts)
    dt = utc.localize(dt)
    x  = int(random.random() * 9)

    if x == 0 or x == 7 or x == 8 :

        foo = None
        my_date = str(ts)

    elif x == 1 :

        foo = dt.astimezone(madrid)
        my_date = foo.strftime(fmt) + ", Madrid"

    elif x == 2 :

        foo = dt.astimezone(londres)
        my_date = foo.strftime(fmt) + ", Londres"

    elif x == 3 :

        foo = dt.astimezone(moscu)
        my_date = foo.strftime(fmt) + ", Moscu"

    elif x == 4 :

        foo = dt.astimezone(tokio)
        my_date = foo.strftime(fmt) + ", Tokio"

    elif x == 5 :

        foo = dt.astimezone(new_york)
        my_date = foo.strftime(fmt) + ", New_York"

    elif x == 6 :

        foo = dt.astimezone(utc)
        my_date = foo.strftime(fmt) + ", UTC"

    print  check(ts,dt,my_date)

    return ts , dt , my_date

def get_the_tz(city):

    if city == "Madrid" :

        rval = madrid

    elif city == "Londres" :

        rval = londres

    elif city == "Moscu" :

        rval = moscu

    elif city == "Tokio" :

        rval = tokio

    elif city == "New_York" :

        rval=new_york

    elif city == "UTC" :

        rval = utc

    else :

        print city
        raise WrongCity

    return rval

def my_date_to_dt(my_date):
    """Converts a string in my format to datetime"""

    # "my format" is just a string containing the date, the format used
    # for the sample file.

    splitted = my_date.split()
    if len(splitted) == 1 :

        ts = int(my_date[0])
        rval = None

    else:

        splitted = my_date.split(",")
        date_and_time = splitted[0]
        the_city = splitted[1]
        the_city = the_city.strip()

        the_date,the_hour = date_and_time.split()

        year , month , day = the_date.split("-")
        hour , minute , seconds = the_hour.split(":")
        year   = int(year)
        month  = int(month)
        day    = int(day)
        hour   = int(hour)
        minute = int(minute)
        print str(year) + "/" + str(month) + "/" + str(day)
        print str(hour) + "/" + str(minute) + "/" + str(seconds) + "/"
        print "city:" + the_city
        new_dt = datetime.datetime(year , month , day , hour , minute)

        print "my_date : " + my_date,
        print "new_dt : " + str(new_dt)
        tz = get_the_tz(the_city)
        new_dt = tz.localize(new_dt)
        new_dt_norm = tz.normalize(new_dt)
        print new_dt , new_dt_norm
        rval = new_dt

    return rval

def check(ts , dt , my_date):
    """Makes sure that we know how to convert datetimes from/to timestamps"""

    new_dt = my_date_to_dt(my_date)

    if new_dt != None:

        new_ts = time.mktime( dt.timetuple())
        new_ts = calendar . timegm ( dt . utctimetuple ( ) ) + 1e-6 * dt . microsecond
        new_ts = calendar . timegm ( dt . utctimetuple ( ) )

        print new_ts
        print ts

        if ts != new_ts:
            rval="ok"
        else:
            rval="error"

    else:

        rval="ok"

    return rval

def my_localize(ts, mytz):
    dt = datetime.datetime.fromtimestamp(ts)
    if mytz == None:
        rval=ts
    else:
        dt   = utc.localize(dt)
        rval = dt.astimezone(mytz)

    return str(rval)

def print_list_as(main_list,city):
    print "------------- ",

    if city==None:
        print "timestamp",
    else:
        print city,
    print "------------- "

    i = 1
    for x in main_list :
        print i,my_localize(x[0],city)
        i = i + 1

def main():
    main_list=[]

    for i in range(TIMES):
        print i + 1,
        x = random_date()
        x = add_city(x)
        main_list.append(x)

    i = 1
    for x in main_list:
        print i,
        i = i + 1
        if x[2]==None:
            print x[0]
        else:
            print x[2]

    raise SystemExit

    print_list_as(main_list,None)
    print_list_as(main_list,madrid)
    print_list_as(main_list,londres)
    print_list_as(main_list,moscu)
    print_list_as(main_list,tokio)
    print_list_as(main_list,new_york)
    print_list_as(main_list,utc)


if __name__ == "__main__":
    main()
