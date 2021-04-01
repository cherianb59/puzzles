# Evaluate a reverse polish notation 
import itertools
from itertools import permutations

def parse_rpn(expression):
	stack = []
 
	for val in expression:
		if val in ['-', '+', '*', '/']:
				op1 = stack.pop()
				op2 = stack.pop()
				if val=='-': result = op2 - op1
				if val=='+': result = op2 + op1
				if val=='*': result = op2 * op1
				if val=='/' and (op1 != 0): result = op2 / op1
				if val=='/' and (op1 == 0): result = 0
				stack.append(result)
		else:
				stack.append(float(val))
 
	return stack.pop()

def solve(numbers):
#generate permutations

	number_permutations=permutations(numbers,4)
	operator_permutations=permutations(operators,3)
	solve = 0 #solved indicator
	
	for number_perm,operator_perm in itertools.product(number_permutations,operator_permutations):
	#	print number_perm
	#	print operator_perm
		number_index = 0
		operator_index = 0
		
		rpn_expression=[]
		for char in expression:
			if char == 'e':
				rpn_expression.append(number_perm[number_index])
				number_index = number_index + 1
			if char == 'o':
				rpn_expression.append(operator_perm[operator_index])
				operator_index = operator_index + 1
		if (parse_rpn(rpn_expression) == 24):
			print(rpn_expression)
			solve = 1
			break
			
	if solve == 0 : 
		print(numbers,"No solutions")		
		
			
#numbers=(0,0,0,0)
operators=['+','-','*','/']

array=[1,2,3,4,5,6,7,8,9,10,11,12,13]
''' 
possible elements and operators arrangements
		eeooo
		eoeoo
		eooeo
		oeoeo
'''
 
expression='eeeeooo'


import time 
start_time=time.time()


for number in itertools.combinations_with_replacement(array, 4):
	solve(number)	

#solve(numbers)	
		
end_time = time.time()
print("time taken=",end_time-start_time)
