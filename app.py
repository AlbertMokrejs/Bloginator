from flask import Flask, render_template, request, session, redirect, url_for
import util

app = Flask(__name__)
app.secret_key = "Something"

def verify():
    if 'log' in session:
        return session['log'] == 'verified'
    else:
        session['log'] = 'unverified'
        return False

@app.route('/')
@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    if verify():
        return redirect(url_for('home'))
    if request.method == "POST":
        form = request.form
        button = form['button']
        if button == "Register":
            return redirect(url_for("register"))
        else:
            uname = form['username']
            session['username'] = uname
            pword = form['password']
            if util.authenticate(uname,pword):
                session['log'] = 'verified'
                session['username'] = uname
                return redirect(url_for('home'))
            else:
                return render_template('login.html', error="Incorrect Username or Password")

@app.route('/register',methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        form = request.form
        uname = form['username']
        pword = form['password']
        button = form['button']
        if button == 'Login':
            return redirect(url_for('login'))
        if util.register(uname,pword):
            session['log'] = 'verified'
            session['username'] = uname
            return redirect(url_for('home'))
        else:
            return render_template('register.html',err="That username is taken!")

@app.route('/home', methods=["GET","POST"])
def home():
    if verify():
        user=''
        if 'username' in session:
            user=session['username']
        else:
            user = session['username'] = "Bleh"
        return render_template('home.html', user=user, posts =util.gettitles())
    return redirect(url_for("login"))

@app.route('/make',methods=["GET","POST"])
def make():
    if request.method =="POST":
        form = request.form
        title=form['Title']
        content=form['content']
        button=form['button']
        user=session['username']
        if button=='Back':
            user=session['username']
            return render_template('home.html', user=user)
        util.add("%s.db"%title,user,content)
        return redirect('/view/%s'%title)
    if verify():
        user = session['username']
        return render_template('make.html',user=user)
    return redirect(url_for("login"))

@app.route('/view')
@app.route('/view/<title>',methods=["GET","POST"])
def view(title=""):
    if title == "":
        return redirect('/home')
    user=""
    if verify():
        user=session['username']
    if request.method == "POST":
        form = request.form
        content = form['content']
        util.add("%s.db"%title,user, content)
    posts = util.getposts(title)
    return render_template('view.html',user=user,title=title,posts=posts)


@app.route('/logout')
def logout():
    if verify():
        session['log'] = "unverified"
    session['action'] = "Logged Out!"
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.debug = True
    app.run()
