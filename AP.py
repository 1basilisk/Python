ap =[]
print("***************** ARITHMATIC PROGRESSION *****************")
a = int(input("first term: "))
d= int(input("common difference: "))
n= int(input("number of terms: "))
l =(a+ (n-1)*d)
print("last term: " + str(l))
for i in range(1,n+1):
	ap.append(a + (i - 1)*d)
	i+=1
print("Sum of AP:", end=" ")
sum = sum(ap)
print(sum)
for elt in ap:
	print(elt ,end="   ")