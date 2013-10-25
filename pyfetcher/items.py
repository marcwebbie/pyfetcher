class Media(object):

    def __init__(self):

        self.name = None
        self.season_num = None
        self.episode_num = None
        self.url = None
        self.has_children = None
        # additional metadata
        self.description = None
        self.verbose_name = None
        self.rating = None
        self.year = None
        self.thumbnail = None
        self.director = None
        self.actors = []

    @property
    def code(self):
        if self.season_num and self.episode_num:
            return u's{0:02d}e{1:02d}'.format(self.season_num, self.episode_num)
