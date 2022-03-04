#!/usr/bin/env python3
"""
Module for 0-app.py
0x0A. i18n - Internationalization and localization
Holberton Web Stack programming Spec ― Back-end
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world():
    """ Welcome HTML page """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
