#!/usr/bin/python3
""" rectangle.py """
from models.base import Base


class Rectangle(Base):
    """ the rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ the initializer """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        Base.__init__(self, id)

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self._width = width

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self._height = height

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self._x = x

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self._y = y

    def area(self):
        return self._width*self._height

    def display(self):
        for l in range(self._y):
            print()
        for i in range(self._height):
            print(" "*self._x, end="")
            for j in range(self._width):
                print("#", end="")
            print()

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self._x}/{self._y} - {self._width}/{self._height}"

    def update(self, *args, **kwargs):
        if len(args) != 0:
            try:
                self.id = args[0]
                self._width = args[1]
                self._height = args[2]
                self._x = args[3]
                self._y = args[4]
            except IndexError:
                pass
        else:
            for it in kwargs.items():
                if it[0] == "id":
                    self.id = it[1]
                elif it[0] == "width":
                    self._width = it[1]
                elif it[0] == "height":
                    self._height = it[1]
                elif it[0] == "x":
                    self._x = it[1]
                else:
                    self._y = it[1]

    def to_dictionary(self):
        return {'id':self.id, 'x':self._x, 'y':self._y, 'width':self._width, 'height':self._height}
