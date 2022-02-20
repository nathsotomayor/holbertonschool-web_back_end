#!/usr/bin/env python3
"""
Module for Auth class to manage the API authentication.
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Defines the Auth class """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Args:
            path - string path to validate in `excluded_paths`
            excluded_paths - routes which don't need authentication
        Returns:
        -------
            True if the path is `None`, `excluded_paths` is `None` or if the
            `path` is not in the list of strings `excluded_paths`,
            False otherwise.
        """
        if path and excluded_paths:
            for ex_path in excluded_paths:
                if ex_path.endswith('/') or ex_path.endswith('*'):
                    ex_path = ex_path[:-1]
                if ex_path in path:
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Args:
            request - Flask request object
        Returns:
        -------
            * The value of the header request `Authorization`
            or
            * `None` if request object does not exist or
            doesn’t contain the header key `Authorization`
        """
        if request:
            return request.headers.get('Authorization')
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Args:
            request - Flask request object
        Returns:
        -------
            None
        """
        return None
