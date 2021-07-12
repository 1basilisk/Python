import random as rand
import csv
movies = []
serial = 0
#opens the list of movies and saves in movies[]
with open("movies.csv") as list:
	for movie in list:
		movie = movie.lower()	
		movies.append(movie)
total = len(movies)
#randomly chooses films
for i in range(1000):
	index = (rand.randrange(1000) % total)
	#print(index)
	serial += 1;
	movie = movies[index]
	
	#saves in file
	with open("moviedata.csv", mode="a") as file:
		file.write(f"{serial},{movie}")
	print(movies[index])