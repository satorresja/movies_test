class MoviePlaylist:
    def __init__(self, movies):
        self.movies = movies

    def show_movies(self):
        for movie in self.movies:
            print(str(movie))
