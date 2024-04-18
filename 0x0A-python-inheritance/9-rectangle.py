#!/usr/bin/python3

"""Deffre frefref refre frefre frefer  referf ometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
	"""Rectangle class."""

	def __init__(self, width, height):
		"""Initialize Rectangle.
		Args:
			width (int): The width of the rectangle.
			height (int): The height of the rectangle.
		"""
		super(Rectangle, self).__init__()
		super(Rectangle, self).integer_validator("width", width)
		self.__width = width
		super(Rectangle, self).integer_validator("height", height)
		self.__height = height

	def area(self):
		"""Return the area of the rectangle."""
		return self.__width * self.__height

	def __str__(self):
		"""Return string representation of the rectangle."""
		return "[{}] {}/{}".format(self.__class__.__name__, self.__width, self.__height)
