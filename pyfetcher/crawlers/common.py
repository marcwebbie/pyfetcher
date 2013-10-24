try:
    from urllib.request import urlopen, Request
except:
    # fallback to python2
    from urllib2 import urlopen, Request


class BaseCrawler(object):

    def __init__(self):
        """
        Subclasses of this one should re-define:
            self.name:              Crawler name
            self.site_url:          Crawler url
            self.description:       Crawler description

            search():               search a file by a given query
            get_raw_urls():         get list of urls to video files for a giver url
        """
        self.name = None
        self.description = None
        self.site_url = None

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


class Search(object):

    """
    Search objects hold search results by crawlers

        self.result: list of media retrieved by search
    """

    def __init__(self, result_list):
        self.result_list = Search.normalize(result_list)

    def get_item(code):
        for item in (i for i in result_list if i.code == code):
            # found an element, return the first
            return item

        return None

    @staticmethod
    def normalize(result_list):
        """ Add code in sequence to choices without code and sort it by code """
        try:
            for idx, item in enumerate(m for m in result_list if not m.code):
                item.code = idx + 1

            return sorted(result_list, key=lambda x: x.code)
        except TypeError:
            sys.stderr.write("ERROR: choices isn't iterable")
            pass
