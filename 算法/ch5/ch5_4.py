def showdata(data_list):
    print('[', end='')
    for i in range(len(data_list)):
        print(data_list[i],end=' ')
    print(']')
class Student:
    def __init__(self,name,age,gpa):
        self.name = name
        self.age = age
        self.gpa = gpa
    def __lt__(self,other):
       return self.gpa < other.gpa
    def __str__(self):
       return f"{self.name} {self.age} {self.gpa}"

def bin_search(data,score):
    low,high = 0,len(data) - 1
    mid = -1
    while not low > high:
        mid = (low+high)//2
        if score > data[mid].gpa:
            high = mid - 1
        elif score < data[mid].gpa:
            low = mid + 1
        else:
            return mid
    return -1

data = [Student("Amy",15,4.2),
        Student("Bill",16,3.8),
        Student("Chris",13,4.0),
        Student("Davud",19,4.8),
        Student("Ed",17,2.6)]

#大到小排序
data.sort(reverse= True)
print("原始資料")
showdata(data)
#輸入成績搜尋
while True:
    score= float(input("輸入成績-1結束"))
    if score == -1.0:
        break
    pos = bin_search(data,score)
    if pos == -1:
        print("無此成績")
    else:
         print(f"找到成績{score}在{pos+1}位置")
