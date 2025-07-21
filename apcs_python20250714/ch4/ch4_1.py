"""
輸入攝氏溫度(輸入q離開):26
攝氏 26度等於華氏 78.80度
輸入攝氏溫度(輸入q離開):18
攝氏 18度等於華氏 64.40度
輸入攝氏溫度(輸入q離開):11
攝氏 11度等於華氏 51.80度
輸入攝氏溫度(輸入q離開):q
程式結束
"""
def c2f(c):
    f = 9/5*c+32
    return f
while True:
    intStr = input("輸入攝氏溫度(輸入q離開):")
    if intStr == 'q':
        print("程式結束")
        break
    tc = int(intStr)
    tf = c2f(tc)
    print(f"攝氏 {tc}度等於華氏 {tf:.2f}度")    
#使用函式完成轉換公式
#f = 9/5*c+32
