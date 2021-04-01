
import random
import time

#winning limits
lower=-1
upper=300

#number of simulations
trials=100000

#make an array to store number of flips for each simulation
history=[]

#simulation counter
count=0

while count<trials:
	score=0
	flips=0
	
	#simulate game
	while (score != lower) and (score != upper):
		
		#flip coin
		flips = flips + 1
		if (random.random()<0.5):
			score = score + 1
		else:
			score = score - 1
			
		#print("Score:",score)
		#time.sleep(1)
		
	#print("count:",count)
	count = count + 1
	history.append(flips)

average_flips = (sum(history) + 0.0) / (trials + 0.0)
print(sum(history))
print("Average flips:",average_flips)
