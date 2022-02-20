#!/usr/bin/env python3
"""
Module for 3. MRU Caching - Most recently used
0x03. Caching
Holberton Web Stack programming Spec ― Back-end
"""
from collections import deque

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache (BaseCaching):
    """
    Defines a the class MRUCache , which inherits from BaseCaching
    and is a caching system (MRUCache).
    """
    def __init__(self):
        super().__init__()
        self.__stack = deque()

    def put(self, key, item):
        """
        Assigns to the dictionary `self.cache_data` the `item` value
        for the key `key`.
        """
        if key and item:
            if key in self.cache_data:
                self.__stack.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.discard(key)

            self.__stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value in `self.cache_data` linked to `key`
        or `None` if the key doesn’t exist in `self.cache_data`.
        Keeps track of used items.
        """
        if key in self.cache_data:
            self.__stack.remove(key)
            self.__stack.append(key)
            return self.cache_data.get(key)
        return None

    def discard(self, key):
        """
        Discards item according cache replacement policies: MRUCache
        """
        removed = self.__stack.pop()
        del self.cache_data[removed]
        print(f"DISCARD: {removed}")
