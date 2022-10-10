class SampleClass:
    x = 0
    def __init__(self):
        self.y = 10
        
    def change_object(self,new_x,new_y):
        print(self.y)
        self.y = new_y
        
        print("class:",self.__class__)
        print("class attribute x: " , self.__class__.x)
        
        self.__class__.x = new_x
    
    @classmethod
    def change_class(cls):
        print("Class Attribute X", cls.x)
        cls.x = 1000
    
    @staticmethod    
    def auxiliary_method():
        print("inside static method")
        
# print("Class Attribute X" , SampleClass.x)

# obj = SampleClass()
# obj.change_object(50,100)

# print("Class Attribute X",SampleClass.x)
# print("Instance Attribute Y", obj.y)

# print("Class Attribute before the call:", SampleClass.x)
# SampleClass.change_class()
# print("Class Attribute after the call:", SampleClass.x)

SampleClass.auxiliary_method()
obj = SampleClass()
obj.auxiliary_method()