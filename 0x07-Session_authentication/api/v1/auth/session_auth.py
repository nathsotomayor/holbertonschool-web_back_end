#!/usr/bin/env python3
"""
Module for BasicAuth class to manage the API authentication.
"""
from api.v1.auth.auth import Auth
from typing import TypeVar
from models.user import User
import uuid


class SessionAuth(Auth):
    """ Defines the SessionAuth class that inherits from Auth """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Documentation for a method"""
        if not user_id or type(user_id) != str:
            return None
        session_id = str(uuid.uuid4())
        SessionAuth.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Documentation for a method"""
        if not session_id or type(session_id) != str:
            return None
        return SessionAuth.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> TypeVar('User'):
        """Documentation for a method"""
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        return User.get(user_id)

    def destroy_session(self, request=None):
        """
        Deletes the user session / logout
        """
        if not request:
            return False
        session_id = self.session_cookie(request)
        if not session_id:
            return False
        user = self.user_id_for_session_id(session_id)
        if not user:
            return False
        else:
            del SessionAuth.user_id_by_session_id[session_id]
            return True
