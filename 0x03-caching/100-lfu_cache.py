#!/usr/bin/env python3
"""
Module for 5. LFU Caching
0x03. Caching
Holberton Web Stack programming Spec ― Back-end
"""
from collections import deque

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    Defines a the class LFUCache, which inherits from BaseCaching
    and is a caching system (LFUCache).
    """
    def __init__(self):
        super().__init__()
        self.__queue = deque()
        self.__count = {}

    def put(self, key, item):
        """
        Assigns to the dictionary `self.cache_data` the `item` value
        for the key `key`.
        """
        size = len(self.cache_data)
        if key and item:
            if size >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                self.discard()
            self.cache_data[key] = item
            self.count(key)

    def get(self, key):
        """
        Returns the value in `self.cache_data` linked to `key`
        or `None` if the key doesn’t exist in `self.cache_data`.
        """
        if key in self.cache_data:
            self.__count[key] += 1
            return self.cache_data.get(key)
        return None

    def discard(self):
        """
        Discards item according cache replacement policies: LFUCache
        """
        removed = self.least_frequent()
        del self.cache_data[removed]
        del self.__count[removed]
        print(f"DISCARD: {removed}")

    def least_frequent(self):
        """
        Returns the least frequent used item
        """
        LFU = min([value for value in self.__count.values()])
        for key in self.__count.keys():
            if self.__count[key] == LFU:
                return key

    def count(self, key):
        """
        Keeps track of the frequency of use of the items.
        """
        if key in self.__count:
            self.__count[key] += 1
        else:
            self.__count[key] = 1
