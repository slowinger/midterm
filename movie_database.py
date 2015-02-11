import csv
from urllib.request import urlopen
import json


class Movie:

    def read_file(file_input):

        with open(file_input, "r", encoding="utf-8") as input_csv:
            movie_list = csv.reader(input_csv)
            movies = []
            for line in movie_list:
                new_movie = Movie()
                new_movie.imdb_id = line[0]
                new_movie.title = line[1]
                new_movie.director = line[2]
                new_movie.imdb_rating = float(line[3])
                movies.append(new_movie)
        return movies

    def find_highest_rated(file):

        from_movies = Movie.read_file(file)
        best_movie = Movie()
        best_movie.imdb_rating = float(0)
        for m in from_movies:
            if m.imdb_rating > best_movie.imdb_rating:
                best_movie = m
        return best_movie

    def plot(self):

        webservice_url = "http://www.omdbapi.com/?i=%s&plot=short&r=json" \
            % (self.imdb_id)
        data = urlopen(webservice_url).read().decode("utf8")
        result = json.loads(data)
        plot = result['Plot']
        return plot
