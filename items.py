class BaseMedia(object):

    def __init__(self):
        self.name = None
        self.description = None
        self.rating = None
        self.year = None
        self.thumbnail = None
        self.director = None
        self.actors = []
        self.url = None


class Film(BaseMedia):

    def __init__(self):
        # super().__init__(self)
        super(Film, self).__init__()


class Serie(BaseMedia):

    def __init__(self):
        self.seasons = []
        # super().__init__(self)
        super(Serie, self).__init__()


class Season(BaseMedia):

    def __init__(self):
        self.episodes = []
        self.number = None
        # super().__init__(self)
        super(Season, self).__init__()


class Episode(BaseMedia):

    def __init__(self):
        self.number = None
        self.season_num = None
        # super().__init__(self)
        super(Episode, self).__init__()

    @property
    def code(self):
        return u's{0:02d}e{1:02d}'.format(self.season_num, self.number)
