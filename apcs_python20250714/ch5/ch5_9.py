scores = {"ch":100,"En":80,"Ma":95}
print(scores["ch"])
#print(scores["Os"])
print(scores.get("ch"))
print(scores.get("Os",-1))#key不存在可回傳預設值
