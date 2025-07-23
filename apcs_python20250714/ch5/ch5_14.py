class Employee:
    company = "GJ"
    phone = "(02)2311-4537"#static變數
    def __init__(self,name,salary=20000):
        self.name = name
        self.salary = salary 
    def printInfo(self):
        print("==員工資訊==")
        print("姓名:",self.name)
        print("薪水:",self.salary)
        print("電話:",Employee.phone)
            
emp1 = Employee("Sean",60000)
emp2 = Employee("David")
emp1.printInfo()
emp2.printInfo()
emp1.name = "Ken"
Employee.phone = "8825252"
emp1.printInfo()
emp2.printInfo()
