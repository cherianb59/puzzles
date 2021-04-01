
import random 
import time 
import numpy as np
#from scipy.stats import binom 
binom = np.random.binomial

start_time=time.time()

p = (1.0/2)	 # chance of winning
initial_dice = 7 # number of dice to start with
total_turns = 0
sims = 10000000

def roll_dice(dice, rolls):
	if dice == 0:
		return(rolls)
	else:
		rolls = rolls + 1
		set_dice = binom(dice,p,1)
#		print(set_dice)
		return(roll_dice(dice - set_dice, rolls))

		
for i in range(sims):
#	print("sim",i)
	total_turns = total_turns + roll_dice(initial_dice , 0 )

end_time = time.time()
print("time taken=",end_time-start_time)

average_turns = float(total_turns)/sims	
print("Average rolls with ",initial_dice,"dice and probability", p ," :",average_turns)