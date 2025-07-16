score = 50

if score >= 60:
    print("及格")
    if score >= 90:
        print("好棒棒")
    elif score >= 80:
        print("不錯優")
    else:
        print("還可以")
else:
    print("不及格")
    if score >= 40:
        print("補考")
    else:
        print("重修")
print("分數:",score)        
