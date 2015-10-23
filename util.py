import sqlite3
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
        conn = MongoClient()
        c = conn[filename]
        q = {'user':username, 'content':content}
        c.main.insert(q)
        
def getTables():
        onlyfiles=[f for f in listdir('tables/') if isfile(join('tables/',f))]
        return onlyfiles

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

def register(uname,pword):
        ##should be fine. These ****s used encryption, I think. It makes the code so gross.
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

def getposts(title):
        conn = sqlite3.connect('tables/%s.db'%title)
        c = conn.cursor()
        out = ""
        q = 'SELECT user, content FROM content'
        info = c.execute(q).fetchall()
        conn.commit()
        return info

def gettitles():
    titles = []
    for f in listdir('tables/'):
        if f.find('.db') >= 0:
            titles.append(f[:-3])
    return titles
