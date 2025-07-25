txt = '''床前明月光
疑是地上霜
舉頭望明月
低頭思故鄉'''
try:
    file = open("output2-20250725.txt","w")
    file.write(txt)
    file.close()
    print("寫出成功")
except:
    print("寫出失敗")
