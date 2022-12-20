#!/usr/bin/python3
"""represents a class Square"""


class Square:
    """represents a square"""

    def __init__(self, size=0):
        """initializing the data"""
        self.__size = size

    @property
    def size(self):
        """Retrieving the  size."""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size to a value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")

        self.__size = value

    def area(self):
        """returns the area of square"""
        result = self.__size * self.__size
        return result

    def my_print(self):
        """prints a square with the character #."""
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print()
