import random as rand
import csv
movies = []
genres = []
serial = 0
#opens the list of movies and saves in movies[]
with open("movies.csv") as list:
	for movie in list:
		movie = movie.lower()	
		movies.append(movie)
total_movies = len(movies)

with open("genres.csv") as list:
	for genre in list:
		genre = genre.lower()
		genres.append(genre)
total_genres = len(genres)

#randomly chooses films
for i in range(1000):
	index = (rand.randrange(1000) % total_movies)
	g1 = (rand.randrange(1000) % total_genres)
	g2 = (rand.randrange(1000) % total_genres)
	g3 = (rand.randrange(1000) % total_genres)

	genre1 = genres[g1].strip()
	genre2 = genres[g2].strip()
	genre3 = genres[g3].strip()
	serial += 1
	movie = movies[index].strip()
	#print(f"{serial},{movie},{genre1} {genre2} {genre3}\n")
	#saves in file
	with open("moviedata.csv", mode="a") as file:
		file.write(f'{serial},{movie},{genre1} {genre2} {genre3}\n')
