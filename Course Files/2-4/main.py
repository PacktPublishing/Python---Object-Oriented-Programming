from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self,color):
        self.color = color
    
    @abstractmethod
    def area(self):
        # raise NotImplementedError(f"area method is not defined for {self.__class__.__name__}")
        pass
    
    def get_color(self):
        return self.color
    

class Circle(Shape):
    def __init__(self,color, radius):
        super().__init__(color)
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius **2

        
class Rectangle(Shape):
    def __init__(self,width , height, color):
        super().__init__(color)
        self.width = width
        self.height = height
        
    def area(self):
        return self.width *self.height

c1 = Circle("red", 10)
r1 = Rectangle(2,3,"blue")

print(f"Area {c1.area()}")
print(f"Area {r1.area()}")
