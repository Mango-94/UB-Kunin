string = input()
k = 0
for i in string.split(" "):
	if i.strip()[0] == 'е':
		k += 1
print(k)
