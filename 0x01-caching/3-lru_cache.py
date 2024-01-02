#!/usr/bin/env python3
'''Task 3 involves implementing LRU Caching.
'''


from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    ''' Develop a caching system, 
        `LRUCache`, inheriting from `BaseCaching` class.
    '''

    def __init__(self):
        '''init cache
        '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Will adds an item in_cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lru_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ will retrieve an item by_key.
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)