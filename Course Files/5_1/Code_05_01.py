def linear_model(a,b,x):
    return a*x+b

out1 = linear_model(2,3,0)
out2 = linear_model(2,3,10)

print(out1)
print(out2)


class LinearModel():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def compute(self,x):
        output = self.a *x +self.b
        return output
    
    def __call__(self,x):
        output = self.a *x +self.b
        return output

lm = LinearModel(2,3)
# out1= lm.compute(0)
out1 = lm(0)
# out2 = lm.compute(10)
out2 = lm(10)

print(out1)
print(out2)

