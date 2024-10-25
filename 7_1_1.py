from math import *

figure = input('Введите название фигуры: ')
def s():
	if figure == 'круг':
		r = float(input('Радиус круга: '))
		area = pi * (r**2)
		print(area)
	elif figure == 'квадрат':
		a = int(input('Введите сторону квадрата: '))
		area = a**2
		print(area)
	elif figure =='треугольник':
		a = int(input('Введите основание треугольника: '))
		h = int(input('Введите высоту треугольника: '))
		area = (1/2) * a * h
		print(area)
s()

