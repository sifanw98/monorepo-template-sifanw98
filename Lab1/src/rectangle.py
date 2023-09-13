"""
 Sample modified from CS5500, Mike Shah

 A rectangle class
 Note that there is no constructor or destructor,
 so a default one will be created for us.
"""
from abc import ABC, abstractclassmethod

class Shape(ABC):

    @abstractclassmethod
    def set_value(self):
        pass

    @abstractclassmethod
    def area(self):
        pass

class Rectangle(Shape):

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def get_width(self):
        return self._width
    
    def get_height(self):
        return self._height
    
    def set_width(self, x):
        self._width = x

    def set_height(self, x):
        self._height = x

    def set_values(self, x, y):
        self._width = x
        self._height = y

    def area(self):
        return self.width * self.height


if __name__ == "__main__":
    # Create a rectangle object
    rect = Rectangle()

    # Call a member function
    rect.set_values(3, 4)

    # Print out the area function
    print("area:", rect.area())
