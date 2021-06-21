import csv
lyrics = ""
with open("source.txt") as src:
	read =  csv.reader(src)
	for row in read:
		for char in row:
			lyrics += char
			
with open("lyrics.txt", "w") as file:
	file.write(lyrics)
	