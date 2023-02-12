from typing import List


class Movie:
    def __init__(
        self, title: str, genres: List[str], actors: List[str], imdb_rating: float
    ):
        self.title = title
        self.genres = genres
        self.actors = actors
        self.imdb_rating = float(imdb_rating) if imdb_rating else 0

    def __str__(self) -> str:
        return self.title
