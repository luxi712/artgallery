# ---- YOUR APP STARTS HERE ----
# -- Import section --
from datetime import datetime
from flask import Flask
from flask import render_template
from flask import request


# -- Initialization section --
app = Flask(__name__)
# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("nav.html", time=datetime.now)

@app.route('/basquiat')
def basquiat():
    return render_template('basquiat.html', time=datetime.now)


@app.route('/monet')
def monet():
    return render_template('Monet.html', time=datetime.now)


@app.route('/close')
def close():
    return render_template('Close.html', time=datetime.now)


@app.route('/kahlo')
def kahlo():
    return render_template('Kahlo.html', time=datetime.now)


@app.route('/architecture')
def architecture():
    return render_template('architecture.html', time=datetime.now)


@app.route('/sculptures')
def sculptures():
    return render_template('sculptures.html', time=datetime.now)

@app.route('/print')
def print():
    return render_template('print.html', time=datetime.now)
