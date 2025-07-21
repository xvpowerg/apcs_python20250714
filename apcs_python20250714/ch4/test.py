mylist = ["Ken", "Vivin", "Lucy", "Joy"]
msg = ""
for i in mylist:
    msg += i
    if i != mylist[-1]:
        msg += "-"
print(msg)
