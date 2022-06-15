import sys
import data
import result_presentation
from library import Library


if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit(1)
    library = Library(data.feed_initial_data())
    library.run_views_generator()
    movies_num = int(sys.argv[1])
    series_num = int(sys.argv[2])
    result_presentation.display_info(library.top_titles, movies_num, series_num)