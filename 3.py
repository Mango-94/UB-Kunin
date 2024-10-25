import math

x = float(input('Введите переменную x:'))
y = float(input('Введите переменную y:'))
z = float(input('Введите переменную z:'))
s = (1 + (math.sin(x + y)) ** 2) / abs(x - (2 * y) / (1 + (x ** 2) * (y ** 2))) * x ** abs(y) + (math.cos(math.atan(1/z))) ** 2
print(s)
