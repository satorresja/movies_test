from typing import List, Optional

from src.models.movie import Movie


class MovieClassifier:
    def __init__(self, movies: List[Movie]) -> None:
        self.movies = movies

    def classify_by_popularity(self, top: Optional[bool] = True) -> List[Movie]:
        return sorted(self.movies, key=lambda x: x.imdb_rating, reverse=top)

    def _classify_by_attribute(self, attr: str, value: Optional[str]) -> List[Movie]:
        similar_movies = []
        for m in self.movies:
            if value and value in getattr(m, attr):
                similar_movies.append(m)
        return similar_movies

    def classify_by_similar_movies(
        self, genre: Optional[str] = None, actor: Optional[str] = None
    ) -> List[Movie]:
        return self._classify_by_attribute(
            "genres", genre
        ) + self._classify_by_attribute("actors", actor)

    def classify_by_same_actor(self, actor: Optional[str] = None) -> List[Movie]:
        return self._classify_by_attribute("actors", actor)
