import math

X = int(input('Введите первое число: '))
N = int(input('Введите второе число: '))

def f(X, N):
    if N == 0: # если число 0, то возвращаем максимальное значение
        return 1
    return (X ** N) / math.factorial(N) # ищем значение по формуле

print(f(X, N))