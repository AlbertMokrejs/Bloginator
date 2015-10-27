import sqlite3
import random
from pymongo import MongoClient
from os import listdir
from os.path import isfile, join
import md5 

def add(filename, username, content):
#        if not isfile(join('tables/',filename)):
 #               file = open('tables/' + filename, 'w+')
  #              new = sqlite3.connect('tables/' + filename)
   #             c = new.cursor()
    #            q = "CREATE TABLE content (user text, content text)"
     #           c.execute(q)
      #          new.commit()
       #         file.close()
#Mongo stores files in a seperate place, the above code is likely useless
        conn = MongoClient()
        c = conn["main"]
        q = {'user':username, 'content':content}
        c[filename].insert(q)
#not really sure what this method is for, might work though.
        
#def getTables():
 #Likely useless as the files are stored elsewhere.... need a rewrite
       # onlyfiles=[f for f in listdir('tables/') if isfile(join('tables/',f))]
       # return onlyfiles

# WE NEED TO MAKE A FUNCTION THAT GETS THE TABLES FROM WHEREVER MONGO SAVES IT
 

def authenticate(uname, pword):
        ##should be fine
    m = md5.new()
    m.update(pword)
    f = open("tables/users.txt",'r')
    for line in f.readlines():
        if uname == line.split(',')[0] and m.hexdigest() == line.split(',')[1].strip():
            f.close()
            return True
    f.close()
    return False
 #PWords/Unames are stored in a text file which is annoying / gross

def register(uname,pword):
        ##should be fine. They used encryption, I think. It makes the code so gross.
        ##wanna get rid of encryption?
        ##yes, maybe
    m=md5.new()
    m.update(pword)
    f = open("tables/users.txt", 'r')
    for line in f.readlines():
        if uname == line.split(',')[0]:
            return False
    f.close()
    f = open("tables/users.txt",'a')
    #f.write("%s,%s\n"%(uname,m.hexdigest()))
    #I think it looks prettier, does this work?
    f.write("%(user)s,%(phash)s\n"%({"user":uname,"phash":m.hexdigest()}))
    f.close()
    return True

def getposts(title):
        conn = MongoClient()
        c = conn["main"]
        info = c[filename].find({"user": true, "content":true, "_id":false})
        return info
        #might be broken, no idea. No idea what the heck all these things do.

def gettitles():
    titles = []
    for f in listdir('tables/'):
        if f.find('.db') >= 0:
            titles.append(f[:-3])
    return titles
    #This is 100% BROKEN, as our files are stored somewhere else. We'll need to replace this.
    #where the hell does Mongo save files?? I dont get it
    #Google it
