from flask import Flask, render_template, request, session


app = Flask(__name__)
app.secret_key = ""


def verify():
    if session.log:
        return session['log'] == 'verified'
    else:
        session['log'] = 'unverified'
        return False

@app.route('/')
@app.route('/login', methods=["GET","POST"])
def login():
    if verify():
        return redirect(url_for('home'))
    if request.method == "POST":
        if util.authenticate(session['username'], session['password']):
            session['log'] = "verified"
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error="Incorrect Username or Password")
    return render_template('login.html', message=session['action'])

@app.route('/home')
def home():
    if verify():
        user = session['username']
        return render_template('home.html', user=user)
    return redirect(url_for("login"))

@app.route('/logout')
def logout():
    if verify():
        session['log'] = "unverified"
    session['action'] = "Logged Out!"
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.debug = True
    app.run()
