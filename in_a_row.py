import random
import numpy as np

SIMULATIONS=5000000

IN_A_ROW=10

def flip():
	if random.random() <0.5 :
		return "H"
	else:
		return "T"
	
def trial():
	count=0
	while (1==1):
		count=count+1
		
		flip_results=flip()

		if flip_results=="T":
			return count
			
#	if no T then All H hence this many in a row		
		if count==IN_A_ROW:
			return 0
		
		
#zero indicates sucess, intuitive

def simulation():
	
	trial_success=0
	total_trials=0
	total_flips=0
	
	while trial_success==0:
		flips=trial()
		
		trial_success= (flips==0)
		
		total_trials=total_trials+1
		total_flips=total_flips+flips+IN_A_ROW*trial_success
		
	return(total_trials,total_flips)	
	
trial_count=[]
flip_count=[]

simulation_count=1

while simulation_count<SIMULATIONS:

	if simulation_count%10000==0:
		print("Average trials",np.mean(trial_count),"Average flips",np.mean(flip_count))	
	simulation_results=simulation()
	trial_count.append(simulation_results[0])
	flip_count.append(simulation_results[1])
	simulation_count=1+simulation_count
	
print(SIMULATIONS)	
#print(trial_count)	
#print(flip_count)
		


	