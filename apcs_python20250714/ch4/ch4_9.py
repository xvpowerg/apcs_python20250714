a = 5
def func():
    global a #跟python說 變數宣告在全域
    a += 1
    print("func():a=",a)
print("全域:a=",a)
func()
print("全域:a=",a)
