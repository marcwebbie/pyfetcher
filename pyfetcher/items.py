class Media(object):

    def __init__(self, name, category):

        self.name = name
        self.category = category
        self.url = None

        # additional metadata
        self.description = None
        self.season_num = None
        self.episode_num = None
        self.has_children = None
        self.rating = None
        self.year = None
        self.thumbnail = None
        self.director = None
        self.actors = []

    @property
    def verbose_name(self):
        vname = u"{}, [{}]".format(self.name, self.category)
        if self.season_num and self.episode_num:
            return vname + u"[Season {} - Episode {}]".format(self.season_num, self.episode_num)
        return vname

    @property
    def code(self):
        if self.season_num and self.episode_num:
            return u's{0:02d}e{1:02d}'.format(self.season_num, self.episode_num)

    def __repr__(self):
        return u":id:{0}:name:{1}:rating:{2}:url:{3}:thumbnail:{4}".format(
            id(self),
            self.name if self.name else "None",
            self.rating if self.rating else "None",
            self.url if self.url else "None",
            self.thumbnail if self.thumbnail else "None",
        )
