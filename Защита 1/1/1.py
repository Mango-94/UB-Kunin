import math

x = float(input('Введите переменную x:'))
y = float(input('Введите переменную y:'))
z = float(input('Введите переменную z:'))
s = (2 * math.cos(x - (2 / 3))) / (0.5 + (math.sin(y))**2) * (1 + ((z ** 2)/(3 - (z ** 2/5))))
print(s)
