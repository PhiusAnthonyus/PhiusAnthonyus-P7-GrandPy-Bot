from flask import (Flask, Blueprint, flash, g, redirect, render_template)

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('menu.html')
