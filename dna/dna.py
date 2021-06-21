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
	Dlist = list(reader)
with open(sample) as samp:
	seq = samp.read()
	
longest_STR = {}
len_str = 1
for i in len(seq):
		if seq[i] == seq[i:len_str]
		longest_STR[seq:len_str] = 1;
print(longest_STR)
		
		