from flask import Flask, render_template, url_for, redirect, request, abort


app = Flask(__name__)
app.secret_key = 'development key'

global msg
global is_logined

msg = 'Pass'
is_logined = False


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html", msg=msg)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template("signup.html", msg=msg)


@app.route('/checkuser', methods=['POST', 'GET'])
def checkuser():
    if request.method == 'POST':
        if request.form['login-input'] == 'admin':
            msg = 'Successful login!'
            return redirect(url_for('events'))
        else:
            msg = 'Failed to login!'
            is_logined = False
            return render_template("index.html", msg=msg)
    else:
        return redirect(url_for('index'))


@app.route('/events', methods=['GET', 'POST'])
def events():
    return render_template('events.html', log=is_logined)
