"""
Random quadtatic eq solver.
generates and equation automatically.
no. of roots needed can be given by CLA, default is 100.
*****error[0]: all roots are negative?? --- solved
"""
import csv
import random 
import time
import sys
import os

start = time.time() #start timer
print("Running", end ="")
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
		global real  
		real += 1	
		r1 = round(((-b) + (d**(1/2)))/2/a, 3)
		r2 = round(((-b) - (d**(1/2)))/2/a, 3)
	
		#saves to file
		#if r1 == 10:
			#global real
			#real += 1
		with open("qache.csv", mode ="a") as file:
			file.write(f"{a}, {b}, {c}, {d}, {r1}, {r2},\n")
		
		
#counters
real = 0
non_real = 0
count = 0

#CLA
if len(sys.argv) == 1:
	total = 100
else:
	total = int(sys.argv[1])
	
#loop
while(real < total):
	quad()
	count += 1
	
	
#	os.system("clear")

print()	
end = time.time() #end time
time = end - start
print(f"total equations solved:  {count}")
print(f"useful equations solved:  {real}")
print(f"time:  {round(time, 4)} seconds")	
