class Media(object):

    def __init__(self, name, category, url=None):

        self.name = name
        self.category = category
        self.url = url

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
        vname = u"{0}, [{1}]".format(self.name, self.category)
        if self.code:
            return vname + u"[Season {0} - Episode {1}]".format(self.season_num, self.episode_num)
        return vname

    @property
    def code(self):
        if self.season_num and self.episode_num:
            return u's{0:02d}e{1:02d}'.format(self.season_num, self.episode_num)

    def __str__(self):
        return u"Media(name={0}, category={1}, url={2})".format(
            self.name,
            self.category,
            self.url if self.url else "None"
        )

    def __repr__(self):
        return "{0} at {1}".format(str(self), hex(id(self)))


class Stream(object):

    def __init__(self, sid, host, url):
        self.id = sid
        self.host = host
        self.url = url

    def __str__(self):
        fstr = "Stream(sid={0}, host={1}, url={2})"
        return fstr.format(self.id, self.host, self.url)

    def __repr__(self):
        return "{0} at {1}".format(str(self), hex(id(self)))
