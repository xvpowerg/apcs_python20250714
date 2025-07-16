# 練習：字串練習
## 檢查使用者輸入的字串是否為迴文

# True 是迴文
inStr = input("輸入字串")
reStr = inStr[::-1]#字串倒轉
print(inStr == reStr)
