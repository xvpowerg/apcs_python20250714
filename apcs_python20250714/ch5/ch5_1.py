## BMI 計算函式 作業
def calcBMI(h,w):
    return w / ((h/100) **2)

def diagnose(bmi):
    result = "錯誤"
    if bmi > 30:
        result = "胖胖"
    elif bmi > 25:
        result = "過重"
    elif bmi > 18.5:
        result = "正常"
    elif bmi > 0:
        result = "過輕"
    return  result

h = int(input("身高:"))
w = int(input("體重:"))
bmi = calcBMI(h,w)
result = diagnose(bmi)
print(f"bmi:{bmi:.2f} {result}")










    
