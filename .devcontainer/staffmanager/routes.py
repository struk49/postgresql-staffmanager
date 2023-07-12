from flask import render_template
from staffmanager import app, db
from staffmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("base.html")
