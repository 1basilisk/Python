import sys
import csv
	
"""if len(sys.argv) != 3:
	print("Usage: python dna.py database sample")
	sys.exit(-1)
data = sys.argv[1]
sample = sys.argv[2]
"""
data = "databases/small.csv"
sample = "sequences/1.txt"
		
with open(data) as file:
	reader = csv.DictReader(file)
	data_list = list(reader)
with open(sample) as samp:
	seq = samp.read()
print(data_list)	
longest_STR = {}

		
		