#!/usr/bin/env python3
"""
Module for 3-app.py
0x0A. i18n - Internationalization and localization
Holberton Web Stack programming Spec ― Back-end
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Defines the application configuration """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world() -> str:
    """ Welcome HTML page """
    return render_template('3-index.html')


@babel.localeselector
def get_locale() -> str:
    """
    Determines the best match language according suppported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
