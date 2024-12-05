import math

x = float(input('Введите переменную x:'))
y = float(input('Введите переменную y:'))
z = float(input('Введите переменную z:'))
s = ((9 + (x - y) ** 2) ** 1/3) / (x ** 2 + y ** 2 + 2) - math.e ** abs(x - y) * ((math.tan(z)) ** 3)
print(s)
