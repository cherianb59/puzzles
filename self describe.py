import datetime

start_time=datetime.datetime.now()
start=1000000000
end=9999999999
num=start
check=[0,0,0,0,0,0,0,0,0,0]

while (num<end):
	num_list = [int(i) for i in str(num)]
	
	if sum(num_list)==9:
		for count in range (0, 10):
			check[count] = int(num_list[count] == num_list.count(count))
		
		if sum(check) == 10:
			print("done: "+str(num))
			break
		
	if sum(num_list[-5:])==0:
		now_time=datetime.datetime.now()
		print(now_time)
		print(num_list)
		print(check)
		print(sum(check))
		print(str(100*(num-start+0.01)/(end-start))+"% done")
		print("time till done:"+str(now_time+datetime.timedelta(seconds=(now_time-start_time).total_seconds()/((num-start+0.01)/(end-start)))))
		print("")
	num=num+1
	