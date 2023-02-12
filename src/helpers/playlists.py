from typing import List

from src.models.movie import Movie


class MoviePlaylist:
    def __init__(self, movies: List[Movie]) -> None:
        self.movies = movies

    def show_movies(self) -> None:
        for movie in self.movies:
            print(str(movie))
