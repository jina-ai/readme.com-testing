#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fancy_add(x: int, y: int) -> str:
    """
    Add two integer and return a str representation of the addition
    
    EXAMPLE USAGE
    .. code-block:: python
        sum = fancy_add(1, 2) 
        assert sum == "3"

    :param x: a integer
    :param y: a integer
    :return: the string representation of the addition
    """
    return str(x*y)
