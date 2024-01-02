#!/usr/bin/env python3

'''Task 1 involves implementing FIFO caching.
'''


from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    ''' Implement a caching system, FIFOCache, 
        inheriting from the BaseCaching class.
    '''

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        ''' Set the value of the 'item' for the 
            'key' in the 'self.cache_data' dictionary.
        '''

        if key is None or item is None:
            return

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item

    def get(self, key):
        ''' Retrieve the value associated with the 
            'key' from the 'self.cache_data'.
        '''
        return self.cache_data.get(key, None)