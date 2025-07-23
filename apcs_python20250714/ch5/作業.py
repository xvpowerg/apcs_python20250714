class Item:
    def __init__(self,name,price=0):
        self.name = name
        self.price = price
    def __str__(self):
        return f"{self.name}:{self.price}"
    def __lt__(self,other):
        return self.price < other.price
    def __eq__(self,other):
        return self.price == other.price
def printItems(itemList):
    for it in itemList:
        print(it)
    print()    

it1 =  Item("Apple",80)
it2 =  Item("Banana",73)
it3 =  Item("Cherry",120)
it4 =  Item("Kiwi",20)
#作業請倒序排列 由大到小
myList = [it1,it2,it3,it4]
printItems(myList)
myList.sort()
printItems(myList)

