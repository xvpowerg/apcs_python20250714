#
def getResult(s):
    if 60 <= s <= 100:
        print("及格")
    elif 0 <= s < 60:
        print("不及格")
    else:
        #print("錯誤")
        raise Exception("成績錯誤")
    #60~100及格
    #0~59不及格
    #其他 錯誤
        
getResult(50)
getResult(88)
getResult(885)
getResult(-10)
