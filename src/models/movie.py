class Movie:
    def __init__(self, title, genres, actors, imdb_rating):
        self.title = title
        self.genres = genres
        self.actors = actors
        self.imdb_rating = float(imdb_rating) if imdb_rating else 0

    def __str__(self) -> str:
        return self.title
