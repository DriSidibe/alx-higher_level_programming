#!/usr/bin/python3

class Rectangle:
	def __init__(self, width = 0, height = 0):
		self.__width = width
		self.__height = height

	@property
	def width(self):
		return self.__width

	@width.setter
	def width(self, w):
		if type(w) == int:
			if w >= 0:
				self.__width = w
			else:
				raise ValueError("width must be >= 0")
		else:
			raise TypeError("width must be an integer")

	@property
	def height(self):
		return self.__height

	@height.setter
	def height(self, h):
		if type(h) == int:
			if h >= 0:
				self.__height = h
			else:
				raise ValueError("height must be >= 0")
		else:
			raise TypeError("height must be an integer")
