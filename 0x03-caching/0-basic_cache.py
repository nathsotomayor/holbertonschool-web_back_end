#!/usr/bin/env python3
"""
Module for 0. Basic dictionary.
0x03. Caching
Holberton Web Stack programming Spec ― Back-end
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Defines a the class BasicChache, which inherits from BaseCaching
    and is a caching system.
    """
    def put(self, key, item):
        """
        Assigns to the dictionary `self.cache_data` the `item` value
        for the key `key`.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value in `self.cache_data` linked to `key`
        or `None` if the key doesn’t exist in `self.cache_data`.
        """
        return self.cache_data.get(key)
