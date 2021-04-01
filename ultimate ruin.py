import random 
import time 

start_time=time.time()

p = 0.3	 # chance of winning
win_amount = 3.33
starting_capital = 1
sims = 1000000
total_turns = 0

def fair_game(initial_capital):
	turns = 0
	capital = initial_capital
	while capital > 0 :
		turns = turns + 1
		capital = capital - 1 + win_amount * (random.random() < p) #spin the wheel circumvent if statement
#		print capital
#	print turns
	return turns 

	
def martingale(initial_capital):
	turns = 0
	capital = initial_capital
	win = 1 
	bet = 1
	
	while capital > 0 :
		if win == 1: #if hte bet was won start at 1 again
			bet = 1
		else :
			bet = 2 * bet #otherwise double the bet, this might mean that im betting more than the capital that i have
			
		if random.random() < p : #spin the wheel
			win = 1 
			capital = capital + bet 
		else :
			win = 0 
			capital = capital - bet 
		turns = turns + 1
#		print (bet,capital)
#	print turns
	return turns 
	
for i in range(sims):
	total_turns = total_turns + fair_game(starting_capital)

end_time = time.time()
print("time taken=",end_time-start_time)

average_turns = float(total_turns)/sims	
print("Average time to ruin starting with ",starting_capital,"and probability", p ," :",average_turns)
	
	