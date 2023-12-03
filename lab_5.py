"""
program for testing code
"""
from dataclasses import dataclass

@dataclass
class Movie:
    """
     Movie in cinema
    """
    id_: str
    title: str
    ranking: int
    release_date: int
    character_number: int
    ticket_price: int
    comment: int

    def __eq__(self, other):
        if isinstance(other, Movie):
            return (
                self.id_ == other.id_ and
                self.title == other.title and
                self.ranking == other.ranking and
                self.release_date == other.release_date and
                self.character_number == other.character_number and
                self.ticket_price == other.ticket_price and
                self.comment == other.comment
            )
        return False

    def get_all(self):
        """Get all details of the movie."""
        return (f"id_film: {self.id_}, Title: {self.title}, Ranking: {self.ranking}, "
                f"Release date: {self.release_date}, Character number: {self.character_number}, "
                f"Ticket price: {self.ticket_price} UAN, Comment: {self.comment}")

    def get_release_year(self):
        """Get the release year of the movie."""
        return int(self.release_date)

    def __str__(self):
        """String representation of the movie."""
        return f"{self.title} ({self.release_date}), Ranking: {self.ranking}"

class Cinema:
    """Representation of a cinema."""
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __str__(self):
        """String representation of the cinema."""
        return f"Name - {self.name}, Location - {self.location}"

    def see_my_film(self, movie):
        """Get the movie currently showing in the cinema."""
        return f"{self.name} is showing {movie.title}"

def calculate_profit(price, visitor):
    """Calculate the profit based on ticket price and number of visitors."""
    return price * visitor

def select_movie(movies, desired_ranking, character_number):
    """Select movies based on ranking and character number."""
    return [movie for movie in movies if int(movie.ranking) == int(desired_ranking)
            and int(movie.character_number) >= character_number]

def main():
    """Main function."""
    film_1 = Movie("a123", "Oppenheimer", "10", "2023", "12",
                   150, "Один з найкращих фільмів")
    film_2 = Movie("b456", "Interstellar", "5", "2014", "5",
                   100, "Топ в науковій фантастиці")
    film_3 = Movie("c789", "Barie", "10", "2023", "23",
                   150, "Класний фільм")
    film_4 = Movie("d159", "Forsage 10", "8", "2023", "25",
                   200, "Один з найкращих фільмів")

    print("Poster_1", film_1.get_all())
    print("Poster_2", film_2.get_all())
    print("Poster_3", film_3.get_all())
    print("Poster_4", film_4.get_all())

    cinema_1 = Cinema("IMAX", "Lviv, King Cross")
    cinema_2 = Cinema("Planeta Kino", "Lviv, Forum")
    print(f"Cinema 1: {cinema_1}")
    print(f"Cinema 2: {cinema_2}")

    profit = calculate_profit(150, 300)
    print("Profit:", profit)

    selected_movies = select_movie([film_1, film_2, film_3, film_4], "10", 10)

    if selected_movies:
        print("Selected movies:")
        for movie in selected_movies:
            print(movie)
    else:
        print("No movies meet the criteria.")

    sorted_movies = sorted([film_1, film_2, film_3, film_4], key=Movie.get_release_year)
    print("\nMovies sorted by release year:")
    for movie in sorted_movies:
        print(movie)

if __name__ == "__main__":
    main()


#   pylint lab_5_pylint.py
