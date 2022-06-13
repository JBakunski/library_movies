from models import Movie, Series

def feed_initial_data():
    example_library = [
        Movie('Skazani na Shawshank', 1994, 'Drama'),
        Movie('Nietykalni', 2011, 'Drama/Comedy'),
        Movie('Zielona mila', 1999, 'Drama'),
        Movie('Ojciec chrzestny', 1972, 'Drama'),
        Movie('Skazani na Shawshank', 1994, 'Drama'),
        Movie('Dwunastu gniewnych ludzi', 1957, 'Court Drama'),
        Movie('Forrest Gump', 1994, 'Drama/Comedy'),
        Series(8, 3, 'Nasza Planeta', 2019, 'Documentary'),
        Series(8, 4, 'Czarnobyl', 2019, 'Drama'),
        Series(12, 3, 'Czarnobyl', 2019, 'Drama'),
        Series(11, 10, 'Nasza Planeta', 2019, 'Documentary'),
        Series(7, 9, 'Nasza Planeta', 2019, 'Documentary'),
        Series(4, 6, 'Gra o tron', 2011, 'Fantasy'),
        Series(12, 2, 'Gra o tron', 2011, 'Fantasy')
        ]
    return example_library

def get_elements(item_type, complete_list):
    items_list = []
    for item in complete_list:
        if type(item) == item_type:
            items_list.append(item)
    return sorted(items_list, key= lambda item: item.title)

def get_movies(complete_list):
    movies = get_elements(Movie, complete_list)
    return movies

def get_series(complete_list):
    series = get_elements(Series, complete_list)
    return series