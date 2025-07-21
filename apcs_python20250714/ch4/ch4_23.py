myList = ["Ken","Vivin","Lucy","Joy"]
msg = ""
for i in range(len(myList)):
    msg += myList[i]
    if i != len(myList) - 1:
        msg += "-"
print(msg)        

#Ken-Vivin-Lucy-Joy

