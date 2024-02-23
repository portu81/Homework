# Вводим данные сторон треугольника
from math import sqrt
a = float(input())
b = float(input())
c = float(input())
# Находим периметр
P = a + b + c
p = P / 2
# находим по формуле площадь треугольника
S = sqrt(p * (p - a) * (p - b) * (p - c))
print('Периметр треугольника равен', P)
print('Площадь треугольника равна', S)
