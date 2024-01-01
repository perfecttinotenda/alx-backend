#!/usr/bin/env python3
""" The Pagination helper funktion wit turple.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        This will retrieves index range
        from the given page && page size.
    """

    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)