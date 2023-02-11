class MovieClassifier:
    def __init__(self, movies):
        self.movies = movies
    
    def classify_by_popularity(self, top=True):
        return sorted(self.movies, key=lambda x: x.imdb_rating, reverse=top)
    
    def classify_by_similar_movies(self, genre, actor):
        similar_movies = []
        for m in self.movies:
            if genre and genre in m.genres:
                similar_movies.append(m)
                continue
            if actor and actor in m.actors:
                similar_movies.append(m)
        return similar_movies
    
    def classify_by_same_actor(self, actor=None):
        same_actor_movies = []
        for m in self.movies:
            if actor and actor in m.actors:
                same_actor_movies.append(m)
        return same_actor_movies
