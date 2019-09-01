from flask import Flask, render_template, request, url_for, redirect, flash
from main import run

titles = []
cards = []

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    global titles, cards

    user = request.form['username']
    pas = request.form['password']
    titles, cards = run(user, pas)
    if not titles:
        flash(u"Wrong username or password, please try again ... ")
        return redirect(url_for('index'))
    else:
        return redirect(url_for('show'))

@app.route('/balance')
def show():
    return render_template("index.html", titles=titles, cards=cards)

if __name__ == '__main__':
    app.run()