#!/usr/bin/python3
""" class that defines a rectangle """


class Rectangle:
    """ rectangle class defined by width and height """
    def __init__(self, width=0, height=0):
        """initialize instances of rectangle """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Retrieves Rectangle instance: width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of Rectangle instance"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves rcetangle instance: height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of Rectangle instance"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
