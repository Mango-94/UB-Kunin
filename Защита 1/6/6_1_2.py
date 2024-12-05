a = [1, 2, 3, 0, 4]
sr = sum(a)/len(a)
for i in range(len(a)):
	if a[i] == 0:
		a[i] = sr
print('', a)
