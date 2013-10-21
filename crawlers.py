# -*- coding: utf-8 -*-
import re
import sys
try:
    from urllib.request import urlopen, Request
    from urllib.parse import unquote
    from html.parser import HTMLParser
except:
    from urllib2 import urlopen, Request, unquote
    from HTMLParser import HTMLParser
    input = raw_input
    str = unicode
    range = xrange

from pyquery import PyQuery
from items import Film, Serie, Season, Episode


class BaseCrawler(object):

    def __init__(self):
        self.name = None

    @staticmethod
    def fetch_page(url):
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0'
        headers = {'User-Agent': user_agent}
        req = Request(url, data=None, headers=headers)
        response = urlopen(req)
        the_page = response.read()
        return the_page


class TubeplusCrawler(BaseCrawler):

    def __init__(self):
        self.site_url = "http://www.tubeplus.me/"
        super(TubeplusCrawler, self).__init__()  # to be ported

    def get_seasons(self, serie):
        """
        Get a list of seasons for a given serie

        serie (Serie) -> Serie object to search for seasons
        """
        serie_page = self.fetch_page(serie.url)
        pq = PyQuery(serie_page)

        rgx = re.compile(
            r"/player/\d+/(?P<serie>\w+)/season_(?P<season>\d+)/episode_(?P<episode>\d+)/(?P<title>[\w´`\'\",\.]+)")
        links = [a.attrib.get('href') for a in pq('.seasons[href]')]

        # build episodes
        episodes = []
        for link in links:
            link = HTMLParser().unescape(unquote(link))
            episode = Episode()
            title = re.search(rgx, link).group('title')
            episode.name = re.sub('_', ' ', title)
            episode.number = int(re.search(rgx, link).group('episode'))
            episode.season_num = int(re.search(rgx, link).group('season'))

            episodes.append(episode)

        # build seasons
        seasons = []
        for snum in set(e.season_num for e in episodes):
            season = Season()
            season.number = snum
            ep_list = [ep for ep in episodes if ep.season_num == snum]
            season.episodes = ep_list

            # DEBUG
            # print(season.number)
            # for e in ep_list:
            #     print(e.code, e.name)
            # DEBUG
            seasons.append(season)

        # return seasons
        return seasons

    def search_serie(self, search_query):
        """Return a list of Serie objects found by search_query"""

        search_url = "{}search/tv-shows/{}".format(
            self.site_url, search_query.replace(' ', '+'))

        search_page = self.fetch_page(search_url)
        pq = PyQuery(search_page)

        dom_search_list = pq(u".list_item")
        found_series = []
        for dom_item in dom_search_list:
            serie = Serie()

            # set title
            serie.name = pq(dom_item).find('img[border="0"]').show().attr('alt')

            # set description
            desc = pq(dom_item).find('.plot').text()
            serie.description = re.sub('\s', ' ', str(desc))  # remove newlines from description

            # set rating
            try:
                rating = pq(dom_item).find('span.rank_value').text()
                serie.rating = eval(rating)
            except SyntaxError:
                if self.DEBUG:
                    print('error evaluating rating: %s ' % rating)

            # set page url
            href = pq(dom_item).find('a.panel').attr('href')
            serie.url = '{}{}'.format(self.site_url, href)

            found_series.append(serie)

        return found_series

    def search_film(self, search_query):
        raise NotImplemented("Search serie is not implemented")
