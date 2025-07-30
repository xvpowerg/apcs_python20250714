def dec_to_bin(num):
    l = []
    while True:
        num,reminder = divmod(num,2)#可求得商數餘數
        l.append(str(reminder))
        if num == 0:
            return "".join(l[::-1])
def dec_to_oct(num):
    l = []
    while True:
        num,reminder = divmod(num,8)
        l.append(str(reminder))
        if num == 0:
            return "".join(l[::-1])
def dec_to_hex(num):
    base = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    l = []
    while True:
        num,reminder = divmod(num,16)
        l.append(base[reminder])
        if num == 0:
            return "".join(l[::-1])
        
testNum = int(input("輸入10進位"))
print("二進位:",dec_to_bin(testNum))
print("八進位:",dec_to_oct(testNum))
print("16進位:",dec_to_hex(testNum))
