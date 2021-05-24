from application import app 
from flask import render_template

@app.route("/")
def Hello():
    return render_template ("base.html")