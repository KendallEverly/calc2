from flask import Flask, render_template, flash
from calc import calculations

TOPIC_DIT = calculations()
app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("main.html")


@app.route("/dashboard/")
def dashboard():
    flash("Flash Test!!!")
    return render_template("header.html", TOPIC_DIT=TOPIC_DIT)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run()


