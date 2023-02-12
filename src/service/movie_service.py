import json
from typing import List, Optional

from src.domain.movie_classifier import MovieClassifier
from src.helpers.playlists import MoviePlaylist
from src.models.movie import Movie


class MovieService:
    def __init__(self) -> None:
        with open("data/movies.json", "r", encoding="utf-8") as file:
            movies_data = json.load(file)

        self.movies: List[Movie] = [
            Movie(
                title=movie_data["title"],
                genres=movie_data["genres"],
                actors=movie_data["actors"],
                imdb_rating=movie_data["imdbRating"],
            )
            for movie_data in movies_data
        ]
        self.classifier: MovieClassifier = MovieClassifier(self.movies)

    def playlist(self, rating, genre, actors, it_forward) -> None:
        pass

    def playlist_by_popularity(self, sort: Optional[bool] = True) -> None:
        movies = self.classifier.classify_by_popularity(sort)
        playlist = MoviePlaylist(movies)
        playlist.show_movies()

    def playlist_by_similar_movies(
        self, genre: Optional[str] = None, actor: Optional[str] = None
    ) -> None:
        movies = self.classifier.classify_by_similar_movies(genre, actor)
        playlist = MoviePlaylist(movies)
        playlist.show_movies()

    def playlist_by_actors(self, actor: Optional[str] = None) -> None:
        movies = self.classifier.classify_by_same_actor(actor)
        playlist = MoviePlaylist(movies)
        playlist.show_movies()
