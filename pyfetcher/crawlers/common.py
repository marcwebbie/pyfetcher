try:
    from urllib.request import urlopen, Request
except:
    # fallback to python2
    from urllib2 import urlopen, Request


class BaseCrawler(object):

    """ BaseCrawler gives the default interface for crawlers.
    It also add utility functions to be shared by sub classes.

    Sub classes should override:
        get_streams:
        get_children:
        search:
    """

    def __init__(self):
        self.description = None
        self.site_url = None

    @property
    def name(self):
        class_name = self.__class__.__name__.lower().strip('crawler')
        return class_name

    def get_streams(self, media):
        fmsg = 'Method get_streams is not overriden by: {}'
        class_name = self.__class__.__name__
        raise NotImplementedError(fmsg.format(class_name))

    def get_children(self, media):
        fmsg = 'Method get_children is not overriden by: {}'
        class_name = self.__class__.__name__
        raise NotImplementedError(fmsg.format(class_name))

    def search(self, search_query):
        fmsg = 'Method search is not overriden by: {}'
        class_name = self.__class__.__name__
        raise NotImplementedError(fmsg.format(class_name))

    @staticmethod
    def fetch_page(url):
        """
        Download a page using an user agent read it and return its content
        """
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0'
        headers = {'User-Agent': user_agent}
        req = Request(url, data=None, headers=headers)
        response = urlopen(req)
        content = response.read()
        return content
