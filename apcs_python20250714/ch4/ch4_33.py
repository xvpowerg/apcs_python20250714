cars = ['Honda','Toyota','Ford','BMW']
print(cars)
myCar = "Toyota"
cars.remove(myCar)
print(cars)

myCar = "Ford"
cars.remove(myCar)
print(cars)

myCar = "CCCC"#不在List內會出錯
if myCar in cars:
    cars.remove(myCar)
    print(cars)
