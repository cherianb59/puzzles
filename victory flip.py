
import numpy as np

flip_1 = [1,-1]
flip_2 = [2,-2]

LENGTH = 14

def list_generate(length):
	master_list = []
	for i in range((2**LENGTH) ) :
		list=[]
		for j in range(LENGTH):
			if (i>>j)&1 == 0:
				list.append(flip_1)
			else :
				list.append(flip_2)
		master_list.append((list[::-1]))
	return(master_list)

#print(list_generate(LENGTH))

answer = [] 
for list in list_generate(LENGTH):
	
	
	mesh = np.meshgrid(*list,indexing='ij')
	matrix = np.array(mesh).T.reshape(-1,LENGTH)
	sum = np.sum(matrix, axis=1)
	positive = np.count_nonzero(sum>0)
#	print(positive, list)
	answer.append(positive)
#print(float(answer)/(2**LENGTH))
print(np.max(answer))



