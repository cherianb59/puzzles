import random
import numpy as np

B=6
R=4
SIMULATIONS = 1000000
COUNT = 0 

def trial(B,R):
	b = np.ones(B)
	r = -1 * np.ones(R)

	#combine
	combine = np.concatenate((b,r))
	np.random.shuffle(combine)
	#Cumulative Sum
	cumsum=np.cumsum(combine)
	#Check all greater than 0
	#print(combine, int((np.all(cumsum)>0)))
	return(np.all(cumsum)>0)

simulation_count = 1 
while simulation_count<SIMULATIONS:
	COUNT = COUNT + int(trial(B,R))
	
	if simulation_count%100000==0:	
		print("Average success",float(COUNT)/simulation_count)	
		
	simulation_count = simulation_count + 1
print("Total average success:",float(COUNT)/simulation_count)	


