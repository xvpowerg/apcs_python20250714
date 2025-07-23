cars = ['honda','BMW','Toyota','audi']
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)#大到小
print(cars)
cars.sort(key=len)#長度排序
print(cars)
cars.sort(key=lambda v:v.upper())
print(cars)

