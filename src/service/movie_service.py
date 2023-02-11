import json
from src.domain.movie_classifier import MovieClassifier
from src.models.movie import Movie
from src.helpers.playlists import MoviePlaylist

class MovieService:
    def __init__(self) -> None:
        movies_data = []
        with open("data/movies.json", "r") as file:
            movies_data = json.load(file)

        self.movies = [Movie(
            title=movie_data["title"],
            genres=movie_data["genres"],
            actors=movie_data["actors"],
            imdb_rating=movie_data["imdbRating"]
        ) for movie_data in movies_data] 

    def playlist(self, rating, genre, actors, it_forward):
        classifier = MovieClassifier(self.movies)
        playlist = MoviePlaylist(classifier)

    def playlist_by_popularity(self, sort):
        classifier = MovieClassifier(self.movies)
        movies = classifier.classify_by_popularity(sort)
        playlist = MoviePlaylist(movies)
        playlist.show_movies()

    def playlist_by_similar_movies(self, genre=None, actor=None):
        classifier = MovieClassifier(self.movies)
        movies = classifier.classify_by_similar_movies(genre, actor)
        playlist = MoviePlaylist(movies)
        playlist.show_movies()

    def playlist_by_actors(self, actor):
        classifier = MovieClassifier(self.movies)
        movies = classifier.classify_by_same_actor(actor)
        playlist = MoviePlaylist(movies)
        playlist.show_movies()

    
