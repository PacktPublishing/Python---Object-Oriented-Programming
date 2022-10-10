class A:
    def __init__(self):
        print("Inside class A")
        
class B(A):
    pass
        
class C(A):
    def __init__(self):
        print("Inside class C")
        
class D(B,C):
    pass

d1 = D()

    