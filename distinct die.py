import random 
import time

start_time=time.time()
#number of times to run
trials = 1000000
#number of faces on die
die_faces = 5

#total number of rolls
roll_total = 0

#do tiral number of loops
for counter in range(trials):
	roll_counter=0
	#an array which indicates if a number has appeared on the die e.g. if indicators[2] =1 this means the third face has appeared
	indicators=[0] * die_faces
	
	#keep looping until all the faces have appeared
	while sum(indicators) < die_faces:
		#roll hte dice
		roll_counter = roll_counter + 1
		outcome = random.randint(1,die_faces)
		#a face has appeared, set the array position to 1(true) for that face
		indicators[outcome-1] = 1

	roll_total = roll_counter + roll_total

#average number of rolls per trial
ROLL_AVERAGE = float(roll_total) / trials
end_time = time.time()

print("time taken=",end_time-start_time)
print(ROLL_AVERAGE)
