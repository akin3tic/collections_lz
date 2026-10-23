import matplotlib.pyplot as plt
import numpy as np
#Данные для x²: x — целые числа от -10 до 10, y — их квадраты
x = range(-10,11) 
y = [i**2 for i in x]
#Данные для eˣ: a — тот же диапазон целых чисел, b — e в степени a
a = range(-10,11)
b = np.exp(a)
#Данные для ln(x): n — тот же диапазон, m — натуральный логарифм от n
n = range(-10,11)
m = np.log(n)
#Данные для x³: k — целые от -10 до 10, l — их кубы
k = range(-10,11)
l = [z**3 for z in k]
#Создание фигуры с 4 графиками в ряд 
# 1 строка, 4 колонки, размер окна 14×6 дюймов
fig, axes = plt.subplots(1, 4, figsize=(14, 6))
#График 1: x² — синие звёзды, соединённые линией
axes[0].grid(True)
axes[0].plot(x, y, "*-", color="blue", markersize=8)
#График 2: eˣ — красные кресты, соединённые линией
axes[1].grid(True)
axes[1].plot(a, b, "x-", color="red", markersize=8)
#График 3: ln(x) — зелёные ромбы, соединённые линией
axes[2].grid(True)
axes[2].plot(n, m, "d-", color="green", markersize=8)
#График 4: x³ — жёлтые кружки, соединённые линией
axes[3].grid(True)
axes[3].plot(k, l, "o-", color="yellow", markersize=8)
#Показывает окно с графиками
plt.show()