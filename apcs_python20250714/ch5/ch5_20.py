class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}:{self.age}"
    
class Cat(Animal):#繼承
    pass
a1 = Animal("Bobo",2)
print(a1)
c1 = Cat("Kitty",6)
print(c1)
