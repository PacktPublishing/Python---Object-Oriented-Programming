from datetime import  datetime

class Developer:
    LIMIT = 3
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.skills = []
        
    def __str__(self):
        return f"{self.__class__.__name__},{self.name},{self.age},{len(self.skills)}"
    
    def add_skill(self,skill):
        if len(self.skills)<Developer.LIMIT:
            self.skills.append(skill)
            print("skill added successfully")
        else:
            print(f"You can not add more than {Developer.LIMIT} skills")
            
    @classmethod
    def set_limit(cls,limit):
        Developer.LIMIT = limit
    
    @classmethod    
    def from_birthyear(cls, name, birthyear):
        year = Developer.birthyear2age(birthyear)
        return cls(name,year-birthyear)
    
    @staticmethod
    def birthyear2age(birthyear):
        year = datetime.today().year
        return year
        
        
d1 = Developer("Jenifer",20)
d1.add_skill("Python")
d1.add_skill("Java")
d1.add_skill("C++")
Developer.set_limit(4)
d1.add_skill("MATLAB")
print(d1)
            
d2 = Developer.from_birthyear("Alex" , 2000)
d2.add_skill("PHP")
print(d2)

