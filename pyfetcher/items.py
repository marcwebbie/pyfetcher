class BaseMedia(object):

    def __init__(self):
        self.code = None
        self.name = None
        self.description = None
        self.rating = None
        self.year = None
        self.thumbnail = None
        self.director = None
        self.actors = []
        self.retrieved_url = None


class Media(object):

    def __init__(self):

        self.name = None
        self.season_num = None
        self.episode_num = None
        self.url = None
        self.has_children = None

    @property
    def code(self):
        if self.season_num and self.episode_num:
            return u's{0:02d}e{1:02d}'.format(self.season_num, self.episode_num)

        # additional metadata
        self.description = None
        self.rating = None
        self.year = None
        self.thumbnail = None
        self.director = None
        self.actors = []


class Film(Media):

    def __init__(self):
        # super().__init__(self)
        super(Film, self).__init__()


class TvShow(Media):

    def __init__(self):
        self.seasons = []
        # super().__init__(self)
        super(TvShow, self).__init__()

    def append_season(self, season):
        self.seasons.append(season)

    def extend_seasons(self, season_list):
        self.seasons.extend(season_list)

    def get_episode(self, episode_code):
        for ep_found in (e for e in self.episodes if e.code == episode_code):
            # at least one item was found
            return ep_found

    @property
    def episodes(self):
        """ 
        Get a list with all episodes in the list of seasons 
        """
        all_episodes = []
        for se in self.seasons:
            all_episodes.extend(se.episodes)
        return all_episodes


class Season(Media):

    def __init__(self):
        # super().__init__(self)
        super(Season, self).__init__()
        self.episodes = []
        self.number = None

    def get_episode(self, episode_code):
        for ep_found in self.episodes:
            # at least one item was found
            return ep_found[0]

    @property
    def verbose_name(self):
        return u"Season {0}".format(self.number)


class Episode(Media):

    def __init__(self):
        # super().__init__(self)
        super(Episode, self).__init__()
        self.number = None
        self.season_num = None

    @property
    def code(self):
        return u's{0:02d}e{1:02d}'.format(self.season_num, self.number)


def __init__():
    pass
