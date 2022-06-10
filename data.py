from models import Movie, Series

def feed_initial_data():
    example_library = []
    movie_1 = Movie('Skazani na Shawshank', 1994, 'Drama')
    example_library.append(movie_1)
    movie_1 = Movie('Nietykalni', 2011, 'Drama/Comedy')
    example_library.append(movie_1)
    movie_1 = Movie('Zielona mila', 1999, 'Drama')
    example_library.append(movie_1)
    movie_1 = Movie('Ojciec chrzestny', 1972, 'Drama')
    example_library.append(movie_1)
    movie_1 = Movie('Skazani na Shawshank', 1994, 'Drama')
    example_library.append(movie_1)
    movie_1 = Movie('Dwunastu gniewnych ludzi', 1957, 'Court Drama')
    example_library.append(movie_1)
    movie_1 = Movie('Forrest Gump', 1994, 'Drama/Comedy')
    example_library.append(movie_1)

    series_1 = Series(8, 3, 'Nasza Planeta', 2019, 'Documentary')
    example_library.append(series_1)
    series_1 = Series(8, 4, 'Czarnobyl', 2019, 'Drama')
    example_library.append(series_1)
    series_1 = Series(12, 3, 'Czarnobyl', 2019, 'Drama')
    example_library.append(series_1)
    series_1 = Series(11, 10, 'Nasza Planeta', 2019, 'Documentary')
    example_library.append(series_1)
    series_1 = Series(7, 9, 'Nasza Planeta', 2019, 'Documentary')
    example_library.append(series_1)
    series_1 = Series(4, 6, 'Gra o tron', 2011, 'Fantasy')
    example_library.append(series_1)
    series_1 = Series(12, 2, 'Gra o tron', 2011, 'Fantasy')
    example_library.append(series_1)

    return example_library

def get_movies(complete_list):
    movies_list = []
    for item in complete_list:
        if type(item) == Movie:
            movies_list.append(item)
    return sorted(movies_list, key= lambda movie: movie.title)

def get_series(complete_list):
    series_list = []
    for item in complete_list:
        if type(item) == Series:
            series_list.append(item)
    return sorted(series_list, key= lambda series: series.title)