import unittest
from unittest.mock import patch

from src.helpers.playlists import MoviePlaylist
from src.models.movie import Movie

class TestMoviePlaylist(unittest.TestCase):
    def setUp(self):
        self.movies = [
            Movie("Inception", ["Action", "Sci-Fi", "Thriller"], ["Leonardo DiCaprio"], 8.8)
        ]
        self.movie_playlist = MoviePlaylist(self.movies)
        
    @patch('builtins.print')
    def test_show_movies(self, mock_print):
        self.movie_playlist.show_movies()
        expected_output = 'Inception'
        mock_print.assert_called_with(expected_output)