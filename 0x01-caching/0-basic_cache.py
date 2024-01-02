#!/usr/bin/env python3

'''Task 0 focuses on creating a basic dictionary.
'''


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    ''' Implement a caching system, BasicCache, 
        inheriting from the BaseCaching class.
    '''

    def put(self, key, item):
        ''' Set the value of 'item' for the '
            key' in the dictionary self.cache_data.
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        ''' Retrieve the value associated with the 'key' 
            from the dictionary self.cache_data.
        '''

        return self.cache_data.get(key, None)