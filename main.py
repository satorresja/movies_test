from src.service.movie_service import MovieService


def main():
    while True:
        print("Select an option:")
        print("1. Classify by popularity")
        print("2. Classify by similar movies")
        print("3. Classify by same actor")
        print("4. Quit")
        service = MovieService()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            sort = input("Do you want to sort by top/down: ")
            if sort == "top":
                service.playlist_by_popularity(True)
            else:
                service.playlist_by_popularity(False)
        elif choice == 2:
            genre = input("Enter the genre: ")
            if not genre:
                genre = None
            actor = input("Enter the name of the actor (optional): ")
            if not actor:
                actor = None
            service.playlist_by_similar_movies(genre, actor)
        elif choice == 3:
            actor = input("Enter the name of the actor: ")
            if actor:
                service.playlist_by_actors(actor)
        elif choice == 4:
            break
        service = MovieService()


if __name__ == "__main__":
    main()
