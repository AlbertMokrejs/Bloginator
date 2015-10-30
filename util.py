import random
from pymongo import MongoClient
from os import listdir
from os.path import isfile, join
import md5 

def add(filename, username, content, NUMID):
        conn = MongoClient()
        c = conn["main"]
        q = {'user':username, 'content':content, 'NUMID':NUMID}
        c[filename].insert(q)

def register(uname,pword):
    m=md5.new()
    m.update(pword)
    f = open("tables/users.txt", 'r')
    for line in f.readlines():
        if uname == line.split(',')[0]:
            return False
    f.close()
    f = open("tables/users.txt",'a')
    f.write("%(user)s,%(phash)s\n"%({"user":uname,"phash":m.hexdigest()}))
    f.close()
    return True
    
def authenticate(uname, pword):
    m = md5.new()
    m.update(pword)
    f = open("tables/users.txt",'r')
    for line in f.readlines():
        if uname == line.split(',')[0] and m.hexdigest() == line.split(',')[1].strip():
            f.close()
            return True
    f.close()
    return False

def getposts(title):
    conn = MongoClient()
    c = conn["main"]
    info = c[title].find()
    return info

def gettitles():
    conn = MongoClient()
    c = conn["main"]
    titles = []
    B = c.collection_names(False)
    for f in B:
        titles.append(f)
    return titles
