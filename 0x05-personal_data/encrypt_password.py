#!/usr/bin/env python3
"""
Module for 5. Encrypting passwords and 6. Check valid password
0x05-personal_data
Holberton Web Stack programming Spec ― Back-end
"""
import bcrypt


def hash_password(password: str) -> bytes:
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


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Uses `bcrypt` to validate that the provided password matches
    the hashed password.

    Args:
    ----
        hashed_password: bytes type to compare with password
        password: string type to compare with hashed_password
    Returns:
    -------
        True or False
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
