import math

n=50

subtotal = 0

for j in range(n):
	
	i = j + 1
	num = float(math.factorial(2 * i))
	den = ( ((math.factorial(i)) ** 2) * ( 2 ** (2 * i)))
	term = num / den
	 
	#print(i , term , num, den)
	
	subtotal = subtotal + term
	
print(subtotal)
