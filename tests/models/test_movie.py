import unittest

from src.models.movie import Movie


class TestMovie(unittest.TestCase):
    def test_str_method(self):
        movie = Movie("The Matrix", ["Action", "Sci-Fi"], ["Keanu Reeves"], 8.7)
        self.assertEqual(str(movie), "The Matrix")

    def test_movie_with_empty_string_rating(self):
        movie = Movie(
            "The Matrix",
            ["Action", "Sci-Fi"],
            ["Keanu Reeves", "Laurence Fishburne"],
            "",
        )
        self.assertEqual(movie.imdb_rating, 0.0)
