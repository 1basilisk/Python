import random

num = lambda :random.randrange(1000) 

f = open("data.csv", "w")
f.close()

with open("data.csv", "a") as file:
	file.write("num1,num2\n")
	for i in range(1000):
		file.write(f"{num()},{num()}\n")
"""
print(num1())
print(num1())
"""