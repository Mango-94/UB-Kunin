N = int(input('Введите первое число: '))
M = int(input('Введите второе число: '))
B = []
# Ввод массива
for i in range(M):
    A = []
    for j in range(N):
        A.append(int(input('Введите число: ')))
    B.append(A)
# Вывод массива и сортировка
for i, row in enumerate(B):
    maxim = minim = 0
    for j, elem in enumerate(row):
        if elem > row[maxim]:
            maxim = j
        if elem < row[minim]:
            minim = j
        row[maxim], row[0] = row[0], row[maxim]
        row[minim], row[-1] = row[-1], row[minim]
print(B)