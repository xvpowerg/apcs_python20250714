txt = '''床前明月光
疑是地上霜
舉頭望明月
低頭思故鄉'''
try:    
    print(txt,file=open("output20250725.txt","w"),end="")
    print("寫出成功")
except:
    print("寫出失敗")
