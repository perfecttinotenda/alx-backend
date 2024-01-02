#!/usr/bin/env python3
"""Implementing LIFO Caching for Task 2.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Defines an object for storing and retrieving items 
        in a dictionary with a Last In, First Out (LIFO) removal 
        mechanism upon reaching the limit.
    """
    def __init__(self):
        """Init cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ will adds an item in_cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """ will retrieves an item by_key.
        """
        return self.cache_data.get(key, None)