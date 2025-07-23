class Employee:
    company = "GJ"
    phone = "(02)2311-4537"#static變數
    count = 0
    def __init__(self,name,salary=20000):
        self.name = name
        self.salary = salary
        Employee.count += 1
    def printInfo(self):
        print("==員工資訊==")
        print("姓名:",self.name)
        print("薪水:",self.salary)
        print("電話:",Employee.phone)
    def getTotal():
        print(Employee.count)
emp1 = Employee("Ken",60000)
emp2 = Employee("Sean")
emp3 = Employee("Iris")
Employee.getTotal()
