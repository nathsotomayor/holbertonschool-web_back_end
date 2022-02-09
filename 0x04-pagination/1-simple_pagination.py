#!/usr/bin/env python3
"""
Module for 1. Simple pagination
0x04-pagination
Holberton Web Stack programming Spec ― Back-end
"""
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Finds the correct indexes to paginate the dataset correctly and returns
        the appropriate page of the dataset (i.e. the correct list of rows).
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        self.__dataset = self.dataset()
        size = len(self.__dataset)
        start, end = index_range(page, page_size)

        if start > size:
            return []
        return self.__dataset[start:min(end, size)]


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
