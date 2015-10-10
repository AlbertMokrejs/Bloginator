from flask import Flask, render_template, request, session


app = Flask(__name__)
app.secret_key = ""

@app.route('/')
@app.route('/login')
def login():


    return render_template('login.html')



if __name__ == '__main__':
    app.debug = True
    app.run()
