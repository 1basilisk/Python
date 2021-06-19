import csv
 
def quad():
	a = float(input("Cofficient of x²:	"))
	b = float(input("Cofficient of x:	"))
	c = float(input("Constant term:	"))
	d = (b**2) - (4*a*c)
	r1 = r2 = 0
	if d>=0:
		r1 = round((-b + (d**(1/2)))/2/a, 3)
		r2 = round((-b - (d**(1/2)))/2/a, 3)
		print("Roots are:	" +str( r1 ) + " AND " +str(r2))

	if d<0: 
		print("No real roots")

		
	with open("quadcache.csv", mode ="a") as file:
		writer = csv.writer(file)
		file.write(f"{a}, {b}, {c}, {d}, {r1}, {r2},\n")
again = ""


while(again == ""):
	quad()
	again = input("Press enter to continue\n any other key to quit\n")
	
	