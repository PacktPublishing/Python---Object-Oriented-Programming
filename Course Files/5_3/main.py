class Student:
    def __init__(self,name):
        self.name = name
        self.grades = {}
        
    def add_course(self, course_name , course_grade):
        self.grades[course_name] = course_grade
        
    def average(self):
        if len(self.grades)==0:
            return -1
        
        else:
            return sum(self.grades.values())/len(self.grades)
        
    def __str__(self):
        return f"Student , {self.name}, {len(self.grades)} , {self.average()}"
    
    def __gt__(self,other):
        # if self.average()>other.average():
        #     return True
        # else:
        #     return False
        if isinstance(other,Student):
            return self.average()>other.average()
        elif isinstance(other,(int,float)):
            return self.average()>other
        else:
            raise ValueError(f"can not compare Student and {other.__class__.__name__}")
        
        
    
    def __le__(self,other):
        # if self.average()>other.average():
        #     return True
        # else:
        #     return False
        return self.average()<=other.average()
    
        
        
        
    
    
s1= Student("Alex")
s2 =Student("Bob")

s1.add_course("math",90)
s1.add_course("programming",98)
s1.add_course("physics", 92)

s2.add_course("math",96)
s2.add_course("geography",88)

print(s1)
print(s2)

if s1<=s2:
    print(f"{s1.name} has lower grades than {s2.name}")
else:
    print(f"{s2.name} has lower grades than {s1.name}")
    
    
if s1>90:
    print(f"{s1.name} is a smart student")
    
if s1>"aaa":
    print("ok")
    
    