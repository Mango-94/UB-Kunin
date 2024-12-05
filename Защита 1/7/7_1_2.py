from random import *

a=[randint(1, 11) for i in range(15)]
b=[randint(1, 11) for i in range(15)]
c=[randint(1, 11) for i in range(15)]

def sar():
	sum1=sum(a)
	sa=sum1/15
	sum2=sum(b)
	sa2=sum2/15
	sum3=sum(c)
	sa3=sum3/15
	print(sum1, sa)
	print(sum2, sa2)
	print(sum3, sa3)
sar()

