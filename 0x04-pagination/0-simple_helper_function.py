#!/usr/bin/env python3
"""
Module for 0. Simple helper function
0x04-pagination
Holberton Web Stack programming Spec ― Back-end
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns
    -------
        tuple of size 2 containing a start index and an end index
        corresponding to the range of indexes to return in a list
        for those particular pagination parameters.

        Page numbers are 1-indexed, i.e. the first page is page 1.
    """
    return (page * page_size - page_size, page_size * page)
