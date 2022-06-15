from models import Movie, Series
import random

class Library:
    def __init__(self, elements):
        self.elements = elements
    
    def get_elements(self, item_type):
        items_list = []
        for item in self.elements:
            if isinstance(item, item_type):
                items_list.append(item)
        return sorted(items_list, key= lambda item: item.title)

    def get_movies(self):
        movies = self.get_elements(Movie)
        return movies

    def get_series(self):
        series = self.get_elements(Series)
        return series
    
    def search(self, title):
        searched_items = []
        for item in self.elements:
            if item.title.lower() == title:
                searched_items.append(item)
        return searched_items
    
    def generate_views(self):
        choosed_item = random.choice(self.elements)
        choosed_item.number_of_plays += random.randrange(1, 100)


    def run_views_generator(self):
        for x in range(10):
            self.generate_views()


    def top_titles(self, number_of_titles, content_type):
        if content_type == 'movie':
            return self.get_top_items(self.get_movies(),number_of_titles)
        elif content_type == 'series':
            return self.get_top_items(self.get_series(),number_of_titles)
    
    def get_top_items(self, titles_list, number_of_titles):
        titles = titles_list
        sorted_titles = sorted(titles, key = lambda title: title.number_of_plays, reverse = True)
        top_titles = sorted_titles[:number_of_titles]
        return top_titles