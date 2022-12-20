#!/usr/bin/python3
"""class representation"""


class Square:
    """represents a square"""
    def __init__(self, size=0):
        """initialize data"""
        self.__size = size
        if size is not int(size):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
