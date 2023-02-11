import unittest
from unittest.mock import patch

from src.domain.movie_classifier import MovieClassifier
from src.helpers.playlists import MoviePlaylist
from src.service.movie_service import MovieService


class MovieServiceTestCase(unittest.TestCase):
    @patch.object(MovieClassifier, "classify_by_popularity")
    @patch.object(MoviePlaylist, "show_movies")
    def test_playlist_by_popularity(
        self, mock_show_movies, mock_classify_by_popularity
    ):
        movie_service = MovieService()
        sort = "desc"
        movie_service.playlist_by_popularity(sort)
        mock_classify_by_popularity.assert_called_with(sort)
        mock_show_movies.assert_called()

    @patch.object(MovieClassifier, "classify_by_similar_movies")
    @patch.object(MoviePlaylist, "show_movies")
    def test_playlist_by_similar_movies(
        self, mock_show_movies, mock_classify_by_similar_movies
    ):
        movie_service = MovieService()
        genre = "Action"
        actor = "Keanu Reeves"
        movie_service.playlist_by_similar_movies(genre, actor)
        mock_classify_by_similar_movies.assert_called_with(genre, actor)
        mock_show_movies.assert_called()

    @patch.object(MovieClassifier, "classify_by_same_actor")
    @patch.object(MoviePlaylist, "show_movies")
    def test_playlist_by_actors(self, mock_show_movies, mock_classify_by_same_actor):
        movie_service = MovieService()
        actor = "Keanu Reeves"
        movie_service.playlist_by_actors(actor)
        mock_classify_by_same_actor.assert_called_with(actor)
        mock_show_movies.assert_called()
