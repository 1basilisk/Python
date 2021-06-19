import sys
import csv
""""if len(sys.argv) != 2:
	print("Usage: python dna.py database sample")
	exit(-1)
data = argv[1]
sample = argv[2]"""
data = "databases/small.csv"
with open(data, mode="r") as file:
	reader = csv.reader(file)
	count = 0
	for line in reader:
		print(line)