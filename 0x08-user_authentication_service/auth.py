#!/usr/bin/env python3
"""
Module for auth.py
0x08. User authentication service
Holberton Web Stack programming Spec ― Back-end
"""
import bcrypt
import uuid
from user import User
from db import DB
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """
    Performs a password hashing using the `bcrypt` package

    Args:
    ----
        password: string type to be hashed
    Returns:
    -------
        a salted, hashed password, which is a byte string.
    """
    # Hash a password with a randomly-generated salt
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """ Creates and returns a string representation of a new UUID """
    return str(uuid.uuid4())


class Auth:
    """ Auth class to interact with the authentication database """
    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Register User in the DB """
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            return self._db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """
        Checks if user exists and validates given password

        Args:
        ----
            email: user's email
            password: user's password
        Returns:
        -------
            True or False
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'),
                                  user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """
        Finds the user corresponding to the email, generates a
        new UUID and stores it in the database

        Args:
        ----
            email: user's email
        Returns:
        -------
            User's session ID or None
        """
        try:
            user = self._db.find_user_by(email=email)
            self._db.update_user(user.id, session_id=_generate_uuid())
            return user.session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> str:
        """ Get User from session ID """
        if not session_id:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """ Delete Session"""
        return self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """ Get reset password token"""
        try:
            user = self._db.find_user_by(email=email)
            self._db.update_user(user.id, reset_token=_generate_uuid())
            return user.reset_token
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """ Update password """
        if not reset_token or not password:
            return None
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            newPwd = _hash_password(password)
            self._db.update_user(user.id, hashed_password=newPwd,
                                 reset_token=None)
        except NoResultFound:
            raise ValueError
