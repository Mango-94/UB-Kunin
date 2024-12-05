N = int(input('Ввод: '))
pos = 0
s = 0
A = []
# Ввод массива
for i in range(N):
    B = []
    for j in range(N):
        B.append(int(input('Введите число: ')))
    A.append(B)
# Вывод массива
for i in range(N):
    for j in range(i + 1, N):
        if A[i][j] > 0:
            pos += 1
            s += A[i][j]
        else:
            continue

print('Сумма:', s)
print('Число:', pos)