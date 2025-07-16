score =  int(input("輸入成績"))
result = ""
if score >= 60:
    result = "及格"
else:
    result = "不及格"
print(result)

#三元運算子
result2 = "及格" if score >= 60 else "不及格"
print(result2)
