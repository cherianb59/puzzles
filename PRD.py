#pseudo random distribution solver,
#want an average of 15%, what is the chance the first trial is successful
def PRD(chance):

	c=chance
	n=1/c
	sum=0
	ev=0

	for i  in range (1, int(n+1) ):
		product=1
		for j in range (1,i+1):
			product=product*(1-(j-1)*c)
	#		print("inner loop:"+str(j))
	#		print("product   :"+str(product))
		ev=ev+(i*i*c*product)
		sum=sum+(i*c*product)
	#	print("outer loop:"+str(i))
	#	print("sum       :"+str(sum))
	return (1/ev)
	

target=0.15
for i in range (1,11):

	result=PRD(test)
	
	if (prev_result < target and result < target ) or (prev_result > target and result > target):
		if result<target:
			test=test+0.01
		if result>target:
			test=test-0.01
	else:
		test=(test+prev_test)/2
	prev_test=test
	prev_result=result
