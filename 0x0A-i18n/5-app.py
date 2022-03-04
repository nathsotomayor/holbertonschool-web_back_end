#!/usr/bin/env python3
"""
Module for 5-app.py
0x0A. i18n - Internationalization and localization
Holberton Web Stack programming Spec ― Back-end
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """ Defines the application configuration """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.before_request
def before_request():
    """ Finds a user if any, and set it as a global on `flask.g.user` """
    g.user = get_user(request.args.get('login_as'))


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world():
    """ Welcome HTML page """
    return render_template('5-index.html')


@babel.localeselector
def get_locale() -> str:
    """
    Determines the best match language according suppported languages
    """
    if request.args.get('locale') in app.config['LANGUAGES']:
        return request.args.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user(login_as: int):
    """
    Returns a user dictionary or `None` if the `ID` cannot be found
    or if `login_as` was not passed
    """
    try:
        int(login_as)
    except Exception:
        return None
    return users.get(int(login_as))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
