import pandas as p
import numpy as n
f = str(input("введите ФИО ", ))
a = str(input("введите адрес "))
t = str(input("введите номер телефона "))
d = str(input("введите дату рождения "))
fatd = [
    {'ФИО': f, 'адрес': a, 'телефон': t, 'дата рождения': d}
]
af = p.DataFrame(fatd)
print(af)
while True:
print("1 чтобы добавить запись  ")
print("2 чтобы удалить запись ")
print("3 чтобы измменить запись")
print("4 чтобы закончить редактирование ")
