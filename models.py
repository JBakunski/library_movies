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
        episode =''
        if int(self.episode) < 10:
            episode = f"E0{self.episode}"
        else:
            episode = f"E{self.episode}"

        season = ''
        if int(self.season) < 10:
            season = f"S0{self.season}"
        else:
            season = f"S{self.season}"
        
        return f"{self.title} {season}{episode}"