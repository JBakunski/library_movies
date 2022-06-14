from models import Movie, Series
import sys
import random
class Library:
    def __init__(self, elements):
        self.elements = elements
    
    def get_elements(self, item_type):
        items_list = []
        for item in self.elements:
            if type(item) == item_type:
                items_list.append(item)
        return sorted(items_list, key= lambda item: item.title)

    def get_movies(self):
        movies = self.get_elements(Movie, self.elements)
        return movies

    def get_series(self):
        series = self.get_elements(Series, self.elements)
        return series
    
    def search(self, title):
        searched_items = []
        for item in self.elementslibrary:
            if item.title.lower() == title:
                searched_items.append(item)
        return searched_items
    
    def generate_views(self):
        choosed_item = random.choice(self.elements)
        choosed_item.number_of_plays += random.randrange(1, 100)


    def run_views_generator(self):
        for x in range(10):
            self.generate_views(self.elements)


    def top_titles(self, number_of_titles, content_type):
        if content_type == 'movie':
            movies = self.get_movies(self.elements)
            sorted_movies = sorted(movies, key = lambda movie: movie.number_of_plays, reverse= True)
            top_movies = sorted_movies[:number_of_titles]
            return top_movies
        elif content_type == 'series':
            series = self.get_series(self.elements)
            sorted_series = sorted(series, key = lambda series: series.number_of_plays, reverse=True)
            top_series = sorted_series[:number_of_titles]
            return top_series