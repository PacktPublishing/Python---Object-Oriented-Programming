class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"Point ({self.x}, {self.y})"
    
    def __add__(self,other):
        if isinstance(other,Point):
            return Point(self.x+other.x , self.y+other.y)
        elif isinstance(other,(int,float)):
            return Point(self.x+other , self.y+other)
        else:
            raise TypeError(f"Unsupported operands for +, between Point and {other.__class__.__name__}")
        
    def __radd__(self,other):
        return self+other
    
    def __sub__(self,other):
        return Point(self.x-other.x , self.y-other.y)
    
    
p1 = Point(2,3)
p2 = Point(4,5)

print(p1)
print(p2)

print("p1+p2:", p1+p2)
print("p1-p2:",p1-p2)
print("p1+10:",p1+10)
# print("p1+str:",p1+"hi")
print("10+p1:",10+p1)
