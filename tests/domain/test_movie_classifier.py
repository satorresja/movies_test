import unittest

from src.domain.movie_classifier import MovieClassifier
from src.models.movie import Movie


class TestMovieClassifier(unittest.TestCase):
    def setUp(self):
        self.movies = [
            Movie(
                title="The Shawshank Redemption",
                actors=["Tim Robbins", "Morgan Freeman", "Bob Gunton"],
                imdb_rating=9.3,
                genres=["Drama"],
            ),
            Movie(
                title="The Godfather",
                actors=["Marlon Brando", "Al Pacino", "James Caan"],
                imdb_rating=9.2,
                genres=["Crime", "Drama"],
            ),
            Movie(
                title="The Dark Knight",
                actors=["Christian Bale", "Heath Ledger", "Aaron Eckhart"],
                imdb_rating=9.0,
                genres=["Action", "Crime", "Drama"],
            ),
            Movie(
                title="The Godfather: Part II",
                actors=["Al Pacino", "Robert De Niro", "Robert Duvall"],
                imdb_rating=9.0,
                genres=["Crime", "Drama"],
            ),
            Movie(
                title="Pulp Fiction",
                actors=["John Travolta", "Uma Thurman", "Samuel L. Jackson"],
                imdb_rating=8.9,
                genres=["Crime", "Drama"],
            ),
        ]
        self.movie_classifier = MovieClassifier(self.movies)

    def test_classify_by_popularity(self):
        # Test when top is True (default)
        sorted_movies = self.movie_classifier.classify_by_popularity()
        self.assertEqual(sorted_movies[0].title, "The Shawshank Redemption")
        self.assertEqual(sorted_movies[-1].title, "Pulp Fiction")

        # Test when top is False
        sorted_movies = self.movie_classifier.classify_by_popularity(top=False)
        self.assertEqual(sorted_movies[0].title, "Pulp Fiction")
        self.assertEqual(sorted_movies[-1].title, "The Shawshank Redemption")

    def test_classify_by_similar_movies(self):
        # Test when genre is specified
        similar_movies = self.movie_classifier.classify_by_similar_movies(
            genre="Drama", actor=None
        )
        self.assertEqual(len(similar_movies), 5)
        self.assertEqual(similar_movies[0].title, "The Shawshank Redemption")

        # Test when actor is specified
        similar_movies = self.movie_classifier.classify_by_similar_movies(
            genre=None, actor="Al Pacino"
        )
        self.assertEqual(len(similar_movies), 2)
        self.assertEqual(similar_movies[0].title, "The Godfather")

        # Test when both genre and actor

    def test_classify_by_same_actor(self):
        movie1 = Movie(
            title="The Matrix",
            imdb_rating=8.7,
            genres=["Action", "Sci-Fi"],
            actors=["Keanu Reeves", "Laurence Fishburne"],
        )
        movie2 = Movie(
            title="The Matrix Reloaded",
            imdb_rating=7.2,
            genres=["Action", "Sci-Fi"],
            actors=["Keanu Reeves", "Laurence Fishburne"],
        )
        movie3 = Movie(
            title="John Wick",
            imdb_rating=7.4,
            genres=["Action", "Thriller"],
            actors=["Keanu Reeves"],
        )
        movie4 = Movie(
            title="The Terminator",
            imdb_rating=8.0,
            genres=["Action", "Sci-Fi"],
            actors=["Arnold Schwarzenegger"],
        )
        movie5 = Movie(
            title="Terminator 2: Judgment Day",
            imdb_rating=8.5,
            genres=["Action", "Sci-Fi"],
            actors=["Arnold Schwarzenegger"],
        )

        movies = [movie1, movie2, movie3, movie4, movie5]
        classifier = MovieClassifier(movies)

        same_actor_movies = classifier.classify_by_same_actor(actor="Keanu Reeves")
        self.assertEqual(len(same_actor_movies), 3)
        self.assertEqual(same_actor_movies[0].title, "The Matrix")
        self.assertEqual(same_actor_movies[1].title, "The Matrix Reloaded")
        self.assertEqual(same_actor_movies[2].title, "John Wick")

        same_actor_movies = classifier.classify_by_same_actor(
            actor="Arnold Schwarzenegger"
        )
        self.assertEqual(len(same_actor_movies), 2)
        self.assertEqual(same_actor_movies[0].title, "The Terminator")
        self.assertEqual(same_actor_movies[1].title, "Terminator 2: Judgment Day")

        same_actor_movies = classifier.classify_by_same_actor(actor="Tom Cruise")
        self.assertEqual(len(same_actor_movies), 0)
