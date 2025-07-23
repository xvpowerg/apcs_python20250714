class Employee:#類別
    pass#先不加內容

emp = Employee()#物件
emp.name = "Sean"
emp.salary = 50000
#屬性定義位置因該在class
#屬性如何定義透過物件
print(emp.name,emp.salary )

emp2 = Employee()
print(emp2.name,emp2.salary )
