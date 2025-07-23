class Student:
    def __init__(self,name,age=10):
        self.name = name
        self.age = age
    def printInfo(self):
        print(self.name,self.age)
st1 = Student("Ken",25)
print(st1.name,st1.age)
st2 = Student("Iris",32)
print(st2.name,st2.age)
st3 = Student("Lucy",15)
st3.printInfo()
