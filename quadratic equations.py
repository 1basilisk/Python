a = float(input("Cofficient of x²:	"))
b = float(input("Cofficient of x:	"))
c = float(input("Constant term:	"))
d = (b**2) - (4*a*c)
if d>=0:
	r1 = (-b + (d**(1/2)))/2/a
	r2 = (-b - (d**(1/2)))/2/a
	print("Roots are:	" +str( r1 ) + " AND " +str(r2))
if d<0: #makes non-real roots by taking roots as string!!
	d = -d
	d  = d**(1/2)
	print("Caution: Non-Real Roots ahead!")
	r1 = ("(" + str(-b) + " ± "   + str(d) + "i)/" + str(2*a))
	print("Roots are:	" +str(r1))	