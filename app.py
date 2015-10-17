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
        print form
        uname = form['username']
        session['username'] = uname
        pword = form['password']
        if util.authenticate(uname,pword):
            session['log'] = 'verified'
            session['username'] = uname
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error="Incorrect Username or Password")
    return render_template('login.html')

@app.route('/home', methods=["GET","POST"])
def home():
    if verify():
        user=''
        if 'username' in session:
            user=session['username']
        else:
            user = session['username'] = "Bleh"
        return render_template('home.html', user=user)
    return redirect(url_for("login"))

@app.route('/make')
def make():
    if verify():
        user = session['username']
        return render_template('make.html',user=user)
    return redirect(url_for("login"))

@app.route('/view',methods=["GET","POST"))
def view():
    if verify():
        user=session['username']
    if request.method == "POST":
        form=request.form
        title=form['title']
        content=form['content']
        util.add(title,user,content)
    return render_template('view.html')


@app.route('/logout')
def logout():
    if verify():
        session['log'] = "unverified"
    session['action'] = "Logged Out!"
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.debug = True
    app.run()
