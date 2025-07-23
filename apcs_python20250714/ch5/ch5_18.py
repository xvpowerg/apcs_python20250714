class Student:
    def __init__(self,name,score=0):
        self.name = name
        self.score = score
    def __str__(self):
        return f"{self.name}:{self.score}"
    def __lt__(self,other):        
        return self.score < other.score
    def __eq__(self,other):
        return self.score == other.score
st1 = Student("Ken",75)
st2 = Student("Iris",88)
print(st1,"<",st2,"=",st1 < st2)
