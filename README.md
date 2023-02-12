# Movie Classifier and Playlist Project

Welcome to the Movie Classifier and Playlist project! In this project, we have a MovieClassifier and MovieService class that allow you to create playlists based on movies and classify them based on different attributes such as rating, genres, actors, and popularity.

Getting Started
These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
You need to have Python 3.6 or higher installed on your computer. You can download it from the official Python website.

Installing
You can either clone this repository or download the code as a zip file and unpack it to your preferred location.

Running the code
In your terminal or command prompt, navigate to the project directory and run the following command:

```python main.py```
## Code Structure
The project has the following structure:

```dailybot_test/
    pylintcr
    main.py
    tox.ini
    requirements.txt
    .gitignore
    .vscode/
        launch.json
        settings.json
    data/
        movies.json
    tests/
        __init__.py
        models/
            test_movie.py
            __init__.py
        service/
            test_movie_service.py
            __init__.py
        helpers/
            test_playlists.py
            __init__.py
        domain/
            __init__.py
            test_movie_classifier.py
    src/
        __init__.py
        models/
            movie.py
            __init__.py
        service/
            __init__.py
            movie_service.py
        helpers/
            playlists.py
            __init__.py
        domain/
            movie_classifier.py
            __init__.py
```
## Classes
The project consists of the following classes:

Movie: This class represents a movie. It has the following attributes: title, genres, actors, and imdb_rating.

MoviePlaylist: This class represents a playlist of movies. It has a movies attribute that stores a list of movies.

MovieClassifier: This class allows you to classify movies based on different attributes such as rating, genres, actors, and popularity.

MovieService: This class allows you to create playlists based on movies and classify them using the MovieClassifier class.

## Methods
The project consists of the following methods:

MovieService.playlist_by_popularity(sort): This method creates a playlist based on the popularity of movies. It takes in a sort parameter which is a boolean value. If it is True, the movies will be sorted in ascending order based on their popularity, if it is False, the movies will be sorted in descending order based on their popularity.

MovieService.playlist_by_similar_movies(genre, actor): This method creates a playlist based on similar movies. It takes in two optional parameters: genre and actor. If the genre parameter is not None, the playlist will contain movies with the same genre as the genre parameter. If the actor parameter is not None, the playlist will contain movies with the same actor as the actor parameter. If both parameters are None, the playlist will contain all movies.

MovieService.playlist_by_actors(actor): This method creates a playlist based on the same actors. It takes in an actor parameter which is a string value that represents the name of the actor. The playlist will contain movies with the same actor as the actor parameter.

## Data
The project uses a movies.json file to store movie data. The file consists of a list of dictionaries where each dictionary represents a movie and has the following keys: title, genres, actors, and imdbRating.

## Running the tests
To run the tests, navigate to the project directory and run the following command: ```python -m unittest```
