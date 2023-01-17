#!/usr/bin/python3
""" square.py """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ the Square class """
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        Rectangle.__init__(self, size, size, x, y, id)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self._size = size
        self._width = size
        self.height = size

    def __str__(self):
        return f"[Square] ({self.id}) {self._x}/{self._y} - {self.size}"

    def update(self, *args, **kwargs):
        if len(args) != 0:
            try:
                self.id = args[0]
                self._size = args[1]
                self._x = args[2]
                self._y = args[3]
            except IndexError:
                pass
        else:
            for it in kwargs.items():
                if it[0] == "id":
                    self.id = it[1]
                elif it[0] == "size":
                    self._size = it[1]
                elif it[0] == "x":
                    self._x = it[1]
                else:
                    self._y = it[1]

    def to_dictionary(self):
        return {'id':self.id, 'size':self._size, 'x':self._x, 'y':self._y}
