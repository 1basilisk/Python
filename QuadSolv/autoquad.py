"""
Random quadtatic eq solver.
generates and equation automatically.
no. of roots needed can be given by CLA, default is 100.
*****error[0]: all roots are negative?? --- solved
"""
import random 
import time
import sys

start = time.time() #start timer

#variables for printing status.
status = False
status_delay = 3 #delay in printing status like "Working on it"
if sys.argv[1] == "help":
	print("Usage: autoquad.py [Equations needed]")
	sys.exit(0)
print("Running")

#Solver function
def quad():
	#eq generation a,b,c  ±1000; a != 0
	a = round(int(random.randrange(-1000, 1000,1)))
	while(a == 0):
		a = round(int(random.randrange(-1000,1000,1)))		
	b = round(int(random.randrange(-1000, 1000,1)), 3)
	c = round(float(random.randrange(-1000,1000,1)), 3)

	#math part -------- error[0]	
	d = (b**2) - (4*a*c)
	if d >= 0:
		r1 = round(((-b) + (d**(1/2)))/2/a, 3)
		r2 = round(((-b) - (d**(1/2)))/2/a, 3)
		if len(sys.argv) == 2:
			global real  
			real += 1	
		else: 
			if r1 == argv[2]:
				global real
				real += 1
		#saves to file
		# with open("qache.csv", mode ="a") as file:
		# 	file.write(f"{a}, {b}, {c}, {d}, {r1}, {r2},\n")
		
		
#counters
real = 0
non_real = 0
count = 0

#CLA reader
if len(sys.argv) == 1:
	total = 100
else:
	total = int(sys.argv[1])
interval = 0

#loop to give required number of solutions
while(real < total):
	quad()
	count += 1

	#timer for printing status
	timer = time.time() - start
	if round(timer) == interval and status == True:
		status = False
	elif status == False:
		print("Working on it...")
		status = True
		interval += status_delay

end = time.time() #timer stop
time = end - start

#Summary printer
print(f"total equations solved:  {count}")
print(f"useful equations solved:  {real}")
print(f"time:  {round(time, 4)} seconds")	
