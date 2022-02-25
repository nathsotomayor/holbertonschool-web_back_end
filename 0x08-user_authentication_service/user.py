#!/usr/bin/env python3
"""
Module for user.py
0x08. User authentication service
Holberton Web Stack programming Spec ― Back-end
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    """ Defines the model/class `User` for the database table `users` """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250))
    reset_token = Column(String(250))
