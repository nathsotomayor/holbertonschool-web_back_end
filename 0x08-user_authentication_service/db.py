#!/usr/bin/env python3
"""
Module for db.py
0x08. User authentication service
Holberton Web Stack programming Spec ― Back-end
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """ Defines Engine and Session instances for the database """
    def __init__(self):
        """ Constructor that sets up the application """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """
        Defines a Session class which will serve as a factory for new
        Session objects and connects it to the engine.

        Returns:
        -------
            `DBSession` instance as a private property
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Defines an user instance and saves it to the database

        Args:
        ----
            email: user's email
            hashed_password:  user's password
        Returns:
        -------
            `User` object
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """
        Searches filtered by the method’s input arguments.

        Args:
        ----
            arbitrary keyworded arguments
        Returns:
        -------
            `User` object
        """
        if not kwargs:
            raise InvalidRequestError
        if not all(key in User.__table__.columns for key in kwargs):
            raise InvalidRequestError
        row = self._session.query(User).filter_by(**kwargs).first()
        if not row:
            raise NoResultFound
        return row

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Locates the user to update, then will update the user’s
        attributes as passed in the method’s arguments and commit
        changes to the database.
        Args:
        ----
            user_id
            arbitrary keyworded arguments
        Returns:
        -------
            None
        """
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if key not in User.__table__.columns:
                raise ValueError
            setattr(user, key, value)
        self._session.commit()
