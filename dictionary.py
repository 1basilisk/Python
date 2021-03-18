alex = {'gender':'male' , 'height':'tall','hair':'blonde',}
print(alex)
alex['gender'] = 'female'
print(alex)
for info in alex:
	print(info)
for info,value in alex.items():
	print(info +":---  "+ value)
	print(value.title())
for info in alex.keys():
	print(info.title())
x = input("Enter new Attribute" + ":  ")
x = x.title()
alex[x]= input("Enter Value of " + x + ":  ")
print(alex)