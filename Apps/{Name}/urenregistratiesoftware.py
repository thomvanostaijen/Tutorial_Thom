"""
Description: main flask file for running this demo app.
Usage:
    run setup.cmd
    Access the website via the given address.
"""
import sys
from flask import Flask, render_template, g, request, jsonify, redirect
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

"""
the form
"""
@app.route("/")
def main():
    return render_template("index.html")
