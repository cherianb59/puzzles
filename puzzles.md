# A list of puzzles I have enjoyed

## Coin Flipping

You and another person are to be locked in separate rooms and are forced to flip a coin every minute. After you flip the coin you have to guess what the other person flipped. If both of you incorrectly guess the other person’s flip you are executed. Before you are locked away you can discuss a strategy to guess each other’s flip.

Is it possible to avoid execution forever?

## Bridges of Konnigsberg

## Sleeping Beauty
A princess can sleep in four rooms (1,2,3,4) each night. Every night she can only sleep in a room adjacent to the room she slept in the previous night (1 and 4 don’t wrap around).

A prince wants to find the princess but he can only check one room each night.

Can you devise a sequence of rooms for the prince to visit so that he finds the princess (doesn’t matter where she starts or which rooms she moves to the sequence should always find her).

Extra Credit: Can you devise a sequence if there are N rooms instead of 4 rooms.

## Train Bee

Two trains 300km apart are travelling toward each other in a straight line. Train A travels at 60 km/h, Train B travels at 40km/h. A bee starts at train A and moves toward train B at 120km/h, it then turns around and travels back to train A, and then turns around back to Train 	B etc. until the two trains meet. How far did the bee travel?

## Flying Time

Suppose you are flying between two cities and you have the departure and arrival times of your initial and return journey, but they are given in the local city’s time (Just like a return airplane ticket) and the cities are in different time zones.
What is the actual time it takes to travel between the two cities (you don’t know the time zone of either city).

Bonus Question: What is the time zone difference between the two cities?

## Self Descriptive

Find a 10-digit number where the first digit is how many zeros are in the number, the second digit is how many 1s  are in the number etc. until the tenth digit which is how many 9s are in the number.

## River Crossing

A father and his two sons, a mother and her two daughters, a thief and a policeman are on one side of a river. 
There is a boat by the river bank, but it can only take two people at a time. 
Only the father, the mother and the policeman know how to operate the boat. 
The father can not be with any of the girls without their mother around. 
The mother can not be with any of the boys without their father around. 
The thief can not be with anyone else without the policeman around (but he can be alone). 

How can you get everyone across to the other side of the river? 

## Radio Receiver

In the early days of radio all the sound was recorded in mono, one channel was transmitted, one channel was received and the radio receiver played in mono as well. 
Life was simple. Then stereo sound was invented. Broadcasts were recorded in stereo and two channels could be transmitted, two channels could be received and the receiver could play all the left sound in the left channel and all the right sound in the right channel. Not everyone upgraded to stereo, lots of people still had mono receivers.
The engineers had a problem where they wanted to broadcast so people with mono receivers got sound as normal (they weren't listening to the left channel or the right channel),and people with stereo got stereo sound. 
The engineers have control over what gets output from the radio station, and the new stereo receivers, but not the old mono receivers.


The inputs of Transmitter are the recordings (L and R) and the outputs are the the two channels C1 and C2.
The Mono receiver can only receive and play C1 through the speaker. The engineers have decided that C1  = (L+R)/2, the average of the two recordings, this will sound like a normal broad cast to the mono receivers. 
 
The stereo receivers has two inputs, C1 and C2 and can modify these inputs linerarly to output sound to the left and right speakers. 
Your task is to find functions C2=f(L,R) and L =f(C1,C2) R = f(C1,C2) and all the functions have to be linear. 
