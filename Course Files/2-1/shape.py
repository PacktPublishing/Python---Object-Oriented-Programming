class Shape:
    def __init__(self, border_color, border_thickness,  location):
        self.border_color = border_color
        self.border_thickness = border_thickness
        self.location = location
        
    def __str__(self):
        return f"{self.__class__.__name__},- {self.border_color}, {self.border_thickness} , {self.location}"
    
    def change_border_color(self,new_color):
        self.border_color = new_color
        
    def change_border_thickness(self,new_thickness):
        self.border_thickness = new_thickness
        
    
class Circle(Shape):
    def __init__(self,radius , border_color,border_thickness, location):
        self.radius = radius
        super().__init__(border_color,border_thickness, location)
        

    def __str__(self):
        return f"{super().__str__()},{self.radius}"

    def area(self):
        