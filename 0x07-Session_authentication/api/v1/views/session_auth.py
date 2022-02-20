#!/usr/bin/env python3
""" Module for Session Authentication view
"""
from api.v1.views import app_views
from flask import jsonify, request, abort
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_authentication():
    """
        POST /auth_session/login

        Return:
        ------
      - Response Object: User object JSON represented and Cookie for
        Session Authentication
    """
    email, pwd = request.form.get('email'), request.form.get('password')
    if not email:
        return jsonify({"error": "email missing"}), 400
    if not pwd:
        return jsonify({"error": "password missing"}), 400

    try:
        user = User.search({'email': email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404

    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    if not user[0].is_valid_password(pwd):
        return jsonify({"error": "wrong password"}), 401
    else:
        from api.v1.app import auth
        #  Get session ID [string] from SessionAuth.create_session:
        session_id = auth.create_session(user[0].id)
        #  jsonify() returns a Response object, so capture it before returning
        #  from the view and add the cookie then with Response.set_cookie:
        response = jsonify(user[0].to_json())
        # environment variable SESSION_NAME as cookie name
        cookie_key = getenv('SESSION_NAME')
        response.set_cookie(cookie_key, session_id)
        return response


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def session_logout():
    """
        DELETE /api/v1/auth_session/logout

        Return:
        ------
      - Empty Response Object with status code 200 or Abort
    """
    from api.v1.app import auth
    is_logged = auth.destroy_session(request)
    if is_logged:
        return jsonify({}), 200
    else:
        abort(404)
