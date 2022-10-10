class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def __gt__(self,other):
        if isinstance(other, Rectangle):
            return self.area()>other.area()
        elif isinstance(other,(int,float)):
            return self.area()>other
        else:
            raise ValueError(f"> is not supported between Rectangle and {other.__class__.__name__}")
    
if __name__ == "__main":
    r1 = Rectangle(2,3) 
    r2 = Rectangle(3,4)

    if r2>r1:
        print("r2 is greater than r1")
        
    if r1>1:
        print("r1 is greater than 1 m2")
        
    if r1>"hello":
        print("ok")

