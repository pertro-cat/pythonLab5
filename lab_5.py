from enum import Enum

class InvalidMovieDetailsException(Exception):
    pass

class InvalidMovieAdditionallyException(Exception):
    pass

class InvalidMovieException(Exception):
    pass

class CinemaNotFoundException(Exception):
    pass

class InvalidProfitCalculationException(Exception):
    pass

class Genre(Enum):
    ACTION = 2
    COMEDY = 1
    DRAMA = 3
    FANTASY = 5

class MovieDetails:
    """
    movie detals parametrs
    """
    def __init__(self, id, title, ranking, release_date):
        if not (id and title and ranking and release_date):
            raise InvalidMovieDetailsException("Invalid movie details.")
        self.id = id
        self.title = title
        self.ranking = ranking
        self.release_date = release_date

class MovieAdditionally:
    """
    movie additional parametrs
    """
    def __init__(self, character_number, ticket_price, comment):
        if not (character_number and ticket_price and comment):
            raise InvalidMovieAdditionallyException("Invalid movie additionally details.")
        self.character_number = character_number
        self.ticket_price = ticket_price
        self.comment = comment

class Movie(MovieDetails, MovieAdditionally):
    """
    all parametrs
    """
    def __init__(self, id, title, ranking, release_date, character_number, ticket_price, comment):
        if not (id and title and ranking and release_date and character_number and ticket_price and comment):
            raise InvalidMovieException("Invalid movie parameters")
        MovieDetails.__init__(self, id, title, ranking, release_date)
        MovieAdditionally.__init__(self, character_number, ticket_price, comment)

    def getAll(self):
        return (f"id_film: {self.id}, Title: {self.title}, Ranking: {self.ranking}, Release date: {self.release_date},"
                f" Character number: {self.character_number}, Ticket price: {self.ticket_price} UAN, Comment: {self.comment}")
"""
this function calculate profit
"""
def calculateProfit(ticket_price, audience):
    if ticket_price < 0 or audience < 0:
        raise InvalidProfitCalculationException("Invalid profit calculation parameters")
    return ticket_price * audience

def get_release_year(movie):
    return int(movie.release_date)
"""
this function sorted movie
"""
def sort_movies_by_release_year(movies):
    return sorted(movies, key=get_release_year)

class Cinema:
    """
    cinema paremetrs
    """
    def __init__(self, name, location):
        if not (name and location):
            raise CinemaNotFoundException("Your cinema has incorrect parameters")
        self.name = name
        self.location = location

def select_movie(movies, desired_ranking, character_number):
    selected_movies = []

    for movie in movies:
        ranking = int(movie.ranking)

        if ranking == int(desired_ranking) and int(movie.character_number) >= character_number:
            selected_movies.append(movie)

    return selected_movies

def main():
    Film_1 = Movie("a123", "Oppenheimer", "10", "2023",
                   "12", 150, "Один з найкращих фільмів")
    Film_2 = Movie("b456", "Interstellar",
                   "5", "2014", "5", 100, "Топ в науковій фантастиці")
    Film_3 = Movie("c789", "Barie", "10", "2023",
                   "23", 150, "Класний фільм")
    Film_4 = Movie("d159", "Forsage 10", "8", "2023",
                   "25", 200, "Один з найкращих фільмів")

    print("Poster_1", Film_1.getAll())
    print("Poster_2", Film_2.getAll())
    print("Poster_3", Film_3.getAll())
    print("Poster_4", Film_4.getAll())

    Cinema_1 = Cinema("IMAX", "Lviv, King Cross")
    Cinema_2 = Cinema("Planeta Kino", "Lviv, Forum")
    print("Cinema 1: Name -", Cinema_1.name, "Location -", Cinema_1.location)
    print("Cinema 2: Name -", Cinema_2.name, "Location -", Cinema_2.location)

    profit = calculateProfit(150, 300)
    print("Profit:", profit)

    selected_movies = select_movie([Film_1, Film_2, Film_3, Film_4], "10", 10)

    if selected_movies:
        print("Selected movies:")
        for movie in selected_movies:
            print(f"{movie.title} ({movie.release_date}), Ranking: {movie.ranking}")
    else:
        print("No movies meet the criteria.")

    sorted_movies = sort_movies_by_release_year([Film_1, Film_2, Film_3, Film_4])
    print("\nMovies sorted by release year:")
    for movie in sorted_movies:
        print(f"{movie.title} ({movie.release_date})")

def logged(exception, mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except exception as e:
                if mode == 'console':
                    logging.error(f"Exception in {func.__name__}: {e}")
                elif mode == 'file':
                    logging.basicConfig(filename='error_log.txt', level=logging.ERROR)
                    logging.error(f"Exception in {func.__name__}: {e}")
                else:
                    raise ValueError("Invalid logging mode. Use 'console' or 'file'.")
        return wrapper
    return decorator

@logged(InvalidProfitCalculationException, mode='file')
def calculateProfit(price, visitor):
    if price <= 0 or visitor <= 0:
        raise InvalidProfitCalculationException("Invalid profit calculation input.")
    profit_in_day = price * visitor
    return profit_in_day


if __name__ == "__main__":
    main()
