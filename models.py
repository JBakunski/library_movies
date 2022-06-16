class Movie:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre

        self.number_of_plays = 0
    
    def play(self):
        self.number_of_plays += 1
    
    def __str__(self):
        return f"{self.title} ({self.year})"


class Series(Movie):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season

    def __str__(self):       
        return f"{self.title} S{self.season:02d}E{self.episode:02d}"