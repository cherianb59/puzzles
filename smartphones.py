import random

minutes=[1,2,3,4,5]
#minutes=[1,2,3]
simulations=100000

results=[]

for simulation in range(simulations):
	
	player_a_total=0
	player_b_total=0

	#print((player_a_total != player_b_total) ,(player_a_total == 0) and (player_b_total == 0))
	
	while ((player_a_total != player_b_total) or ((player_a_total == 0) and (player_b_total == 0))):
	
		if player_a_total < player_b_total:
			player_a_total = player_a_total+random.choice(minutes)
			
		elif player_a_total > player_b_total:
			player_b_total = player_b_total+random.choice(minutes)
			
		elif player_a_total == player_b_total:
			player_a_total = player_a_total+random.choice(minutes)
			player_b_total = player_b_total+random.choice(minutes)
	
		#print("A: ",player_a_total,"B: ",player_b_total,"Run: ",simulation)
		
		
	results.append(player_a_total)
	average=sum(results)/float(len(results))
	print("Average: ",average)
#print("Average: ",average)	