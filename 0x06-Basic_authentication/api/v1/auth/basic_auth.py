#!/usr/bin/env python3
"""
Module for BasicAuth class to manage the API authentication.
"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """ Defines the BasicAuth class that inherits from Auth """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Extracts Base64 Authorization Header """
        if (
            not authorization_header or type(authorization_header) != str
            or "Basic " not in authorization_header
        ):
            return None
        return authorization_header.split()[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """ Decode Base64 Authorization Header """
        if (
            not base64_authorization_header
            or type(base64_authorization_header) != str
        ):
            return None
        try:
            b64_bytes = base64_authorization_header.encode('utf-8')
            string_bytes = base64.b64decode(b64_bytes)
            return string_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """ Extract User Credentials """
        if (
            not decoded_base64_authorization_header
            or type(decoded_base64_authorization_header) != str
            or ':' not in decoded_base64_authorization_header
        ):
            return None, None
        return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(self,
                                     user_email: str, user_pwd: str
                                     ) -> TypeVar('User'):
        """ User Object From Credentials """
        if (
            not user_email or type(user_email) != str
            or not user_pwd or type(user_pwd) != str
        ):
            return None
        try:
            user = User.search({'email': user_email})
        except Exception:
            return None

        if user and user[0].is_valid_password(user_pwd):
            return user[0]
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current User """
        data = self.authorization_header(request)
        authheader = self.extract_base64_authorization_header(data)
        decoded = self.decode_base64_authorization_header(authheader)
        user, pwd = self.extract_user_credentials(decoded)
        return self.user_object_from_credentials(user, pwd)
