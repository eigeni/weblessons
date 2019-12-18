from flask import render_template
from weble import app

@app.route("/hello")
def hello():
	return "Hello, World!"

@app.route("/")
@app.route("/index")
def index():
	return render_template("session.html")
