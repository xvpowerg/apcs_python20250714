subjs = ["國文","數學","英文"]
scores = [100,80,95]
obj =  zip(subjs,scores)
#print(list(obj))#預覽
for su,sc in obj:
    print(f"{su}分數{sc}分")
