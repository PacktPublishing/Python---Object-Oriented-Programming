class A:
    def __init__(self):
        self.x= 10
    
class B(A):
    def __init__(self):
        super().__init__()
        self.w = 20
        
class C(A):
    def __init__(self):
        super().__init__()
        self.y = 40
        
class D(B,C):
    def __init__(self):
        super().__init__()

d1 = D()

print(d1.x , d1.y , d1.w)

