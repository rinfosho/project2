import requests
import time
def attack(url,numreq,maxConn):
	count=1
	fail_count=0
	x=numreq/maxConn
	statistics=dict()
	for i in range(x):
		for j in range(maxConn):
			start=time.time()
			# try:
			requests.get(url)
			# except requests.get(url,timeout=0.001):
			# 	break
			# 	print"timeout"
			# 	fail_count+=1

			
			#print "Attack number: ", count
			end = time.time()
			#print "time taken is: ", (end-start)
			statistics[str(count)] = (end-start)
			print "Done: ", count
			count+=1
	# requests.map(rs)
	totaltime = sum(statistics.values())
	print "Time taken for tests: ", totaltime," seconds" 
	print "Completed requests: ", numreq-fail_count
	print "Failed requests: ", fail_count
	print "Avg requests per second: ", (len(statistics))/totaltime," [req/s]"

url="http://10.27.8.20:8080/"
attack(url,10000,2000)