#!/usr/bin/python3
""" Module Name: Base_Caching
"""


class BaseCaching():
    """ BaseCaching defines:
      - Caching Boosts Retrieval Speeds.
      - BaseCaching: Framework for Custom Cache Implementations.
      -  Inherit, Customize, Optimize: Tailor for Efficiency.
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Init
        """
        self.cache_data = {}

    def print_cache(self):
        """ Will print cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Will add an item in_cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Geting an item by_key
        """
        raise NotImplementedError("get must be implemented in your cache class")