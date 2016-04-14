#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import sys
import requests
from argparse import ArgumentParser

def getReq (url) :
    data = []

    r = requests.get(url)
    if r.status_code == 200 :
        data = r.json()
    else :
        print "Error : " + str(r.status_code)

    return data


def getUsers () :
    url = "http://jsonplaceholder.typicode.com/users"
    data = []
    user = []
    listUsers = []

    data = getReq(url)

    for x in range (len (data)) :
        user = []
        user.append(data[x]["username"])
        user.append(data[x]["id"])
        listUsers.append(user)

    return listUsers

def getPosts () :
    url = "http://jsonplaceholder.typicode.com/posts"
    data = []

    data = getReq(url)

    for x in range(len(data)) :
        data[x]["userId"]
        data[x]["title"]
        data[x]["body"]
    return data

def findUser(listUsers , user) :
    for x in range (len(listUsers)) :
        if user is listUsers[x][1] :
            return listUsers[x][0]
    return None


def printOut (user , post) :
    print "De: " ,
    print user
    print post["title"]
    print 10*"--" + "---"
    print post["body"]
    print

def userDef (listUsers , posts) :
    user = ""

    for x in range (len(posts)) :
        user = findUser(listUsers , posts[x]["userId"])
        printOut(user , posts[x])

def isUser (userA , userB) :
    return len(userA) == len(userB) and userA in userB

def findUserId(listUsers , user) :
    for x in range (len(listUsers)) :
        if isUser(listUsers[x][0].lower() , user.lower()):
            return listUsers[x][1] , listUsers[x][0]
    return None

def userOpt (listUsers , posts , user) :
    result = ()
    userId = -1
    userName = ""

    result = findUserId(listUsers , user)

    if result == None :
        sys.stderr.write("USER NOT FOUND" + '\n')
        raise SystemExit

    userId = result[0]
    userName = result[1]
    for x in range (len(posts)) :
        if posts[x]["userId"] == userId :
            printOut(userName , posts[x])


def usersPosts (listUsers , posts , args) :


    if args.user == None :
        userDef(listUsers , posts)
    else :
        userOpt(listUsers , posts , args.user)


def main () :
    listUsers = []
    posts = []

    usage = "Uso %prog [opciones]"
    parser = ArgumentParser(usage)

    parser.add_argument("-u" , "--user" , action="store" , dest="user" ,  \
                                help="User to get his posts.")

    args = parser.parse_args()

    listUsers = getUsers()
    posts = getPosts()
    usersPosts(listUsers , posts , args)


if __name__ == "__main__" :
    main()
