from datetime import date

today_date = date.today().strftime('%d.%m.%Y')

def display_top_movies(func, number):
    print(f"{number} Najlepsze Filmy z dnia {today_date}\n----------------------------------")
    top_movies = func(number, 'movie')
    for movie in top_movies:
        print(f"{movie} - with {movie.number_of_plays} views")

def display_top_series(func, number):
    print(f"{number} Najlepsze Seriale z dnia {today_date}\n--------------------------------")
    top_series = func(number, 'series')
    for series in top_series:
        print(f"{series} - with {series.number_of_plays} views")


def display_info(func, movies_num, series_num):
    print("===========================\nBIBLIOTEKA FILMÓW I SERIALI\n===========================\n")
    display_top_movies(func, movies_num)
    print("\n")
    display_top_series(func, series_num)