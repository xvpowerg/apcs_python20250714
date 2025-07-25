txt = '''床前明月光
疑是地上霜
舉頭望明月
低頭思故鄉'''

try:
    with open("output3-20250725.txt",'w') as f:
        f.write(txt)
        print("寫出成功")
except:
    print("寫出失敗")
