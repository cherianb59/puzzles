DOOR_LENGTH=7
DEPTH_LENGTH=10


#array represents the states of the doors, whether the princess could be in them based on the sequence of doors the prince has checked
#position is where the prince is cheking this round
#the new array outputs possible princess locations
#the output for an array position is based on the two adjacent status of the old array
def step(array,position):
	old=array[:]
	
	array[0]= int((old[1]) and not (position==1))
	
#this doesnt apply to first and last door	
	for i in range(len(old[1:-1])):
		array[i+1]= int((old[i] | old[i+2]) and not (position==i+2))
	#	print(array,old,position)	
	array[DOOR_LENGTH-1]= int((old[DOOR_LENGTH-2]) and not (position==DOOR_LENGTH))
	#print(array,old,position)	
	return array

	
def try_sequence(sequence):
#pass a sequence that the prince will try
	depth=0
#initialise the possible places the princess with be, she can be anywhere at teh start	
	princess=[]
	for i in range(DOOR_LENGTH):
		princess.append(1)
	
	empty=[]
	for i in range(DOOR_LENGTH):
		empty.append(0)
		
	while depth<DEPTH_LENGTH and princess != empty:
		#print(princess)
		princess=step(princess,sequence[depth])
		depth=depth+1
		#print(depth)
	if (princess == empty):
		print(sequence)
		success.append(sequence)	
	else:
		fail.append(sequence)

# recursively call function for gradually increasing depths		
def loop(length,array):
	if (length==DEPTH_LENGTH):
		#print array
		#return array
		try_sequence(array)
	else:
		for i in range(DOOR_LENGTH):
			array[length]=i+1
			loop(length+1,array)
	

sequence=[]

#varaible length empty list
for i in range(DEPTH_LENGTH):
	sequence.append(0)

#print sequence

#how to return all the arrays?

success=[]
fail=[]


loop(0,sequence)


#try_sequence([2,3,4,2,3,4])
#try_sequence([2,3,4,5,6,2,3,4,5,6])
#try_sequence([2,3,3,2])

print(len(success))	