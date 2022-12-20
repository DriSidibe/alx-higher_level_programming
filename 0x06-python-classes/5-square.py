#!/usr/bin/python3
"""Write a class Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """ Initialize the attribute : size"""
        self.size = size

    """Getter"""
    @property
    def size(self):
        return (self.__size)

    """Setter"""
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """Create public instance method: area"""
    def area(self):
        sq_area = self.__size ** 2
        return (sq_area)

    """Create public instance method: my_print
    prints square with # character"""
    def my_print(self):
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            print("#" * self.__size)
