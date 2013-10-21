class BaseMedia(object):

    def __init__(self):
        self.name = None
        self.description = None
        self.rate = None
        self.year = None
        self.director = None
        self.actors = []


class Film(BaseMedia):

    def __init__(self):
        super().__init__(self)


class Serie(BaseMedia):

    def __init__(self):
        self.seasons = []
        super().__init__(self)


class Season(BaseMedia):

    def __init__(self):
        self.episodes = []
        self.number = None
        super().__init__(self)


class Episode(BaseMedia):

    def __init__(self):
        super().__init__(self)
