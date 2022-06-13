import random
import sys
import data
import result_presentation

entire_library = data.feed_initial_data()

def search(library, title):
    searched_items = []
    for item in library:
        if item.title.lower() == title:
            searched_items.append(item)
    return searched_items
    

def generate_views(library):
        choosed_item = random.choice(library)
        choosed_item.number_of_plays += random.randrange(1, 100)


def run_views_generator(library):
    for x in range(10):
        generate_views(library)


def top_titles(number_of_titles, content_type):
    if content_type == 'movie':
        movies = data.get_movies(entire_library)
        sorted_movies = sorted(movies, key = lambda movie: movie.number_of_plays)
        sorted_movies.reverse()
        top_movies = sorted_movies[:number_of_titles]
        return top_movies
    elif content_type == 'series':
        series = data.get_series(entire_library)
        sorted_series = sorted(series, key = lambda series: series.number_of_plays)
        sorted_series.reverse()
        top_series = sorted_series[:number_of_titles]
        return top_series
 

if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit(1)
    run_views_generator(entire_library)
    movies_num = int(sys.argv[1])
    series_num = int(sys.argv[2])
    result_presentation.display_info(top_titles, movies_num, series_num)