# import sqlite3
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
# !A!
        conn = MongoClient()
        c = conn["main"]
        q = {'user':username, 'content':content}
        c[filename].insert(q)
#not really sure what this method is for, might work though.
#it requires not making a new file, but instead makes a new table in. 
        
#def getTables():
 #Likely useless as the files are stored elsewhere.... need a rewrite
       # onlyfiles=[f for f in listdir('tables/') if isfile(join('tables/',f))]
       # return onlyfiles

# WE NEED TO MAKE A FUNCTION THAT GETS THE TABLES FROM WHEREVER MONGO SAVES IT
# SEE !A!, it doesn't make multiple files now
 

def authenticate(uname, pword):
        ##should be fine
    m = md5.new()
    m.update(pword)
    #hashes password
    f = open("tables/users.txt",'r')
    for line in f.readlines():
        if uname == line.split(',')[0] and m.hexdigest() == line.split(',')[1].strip():
         #compares hashed password to recorded password
            f.close()
            #ends loop, closes file
            return True
    f.close()
    return False
 #PWords/Unames are stored in a text file which is fine and should hopefully work. 

def register(uname,pword):
        ##should be fine. They used encryption, I think. It makes the code so gross.
        ##wanna get rid of encryption?
        ##No, it's already implemented. We can work around it.
    m=md5.new()
    m.update(pword)
    f = open("tables/users.txt", 'r')
    for line in f.readlines():
        if uname == line.split(',')[0]:
            return False
            #prevents duplicated
    f.close()
    f = open("tables/users.txt",'a')
    #f.write("%s,%s\n"%(uname,m.hexdigest()))
    #I think it looks prettier, does this work?
    f.write("%(user)s,%(phash)s\n"%({"user":uname,"phash":m.hexdigest()}))
    f.close()
    return True
    #returns true if succesful. A false is an error, probably declared on the page. 

def getposts(title):
        conn = MongoClient()
        c = conn["main"]
        info = c[title].find({"user": True, "content":True, "_id":False})
        return info
        #might be broken, no idea. No idea what the heck all these things do. Assuming it is supposed to find a specific post, it might work with !A!.

def gettitles():
    conn = MongoClient()
    c = conn["main"]
    titles = c.collection_names()
    return titles
    #This is 100% BROKEN, as our files are stored somewhere else. We'll need to replace this.
    #where the hell does Mongo save files?? I dont get it
    #Google it
