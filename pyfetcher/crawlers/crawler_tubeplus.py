# -*- coding: utf-8 -*-
import logging
import re
import sys
try:
    from urllib.request import urlopen
    from urllib.parse import unquote, quote_plus, urljoin
    from html.parser import HTMLParser
except:
    from urlparse import urljoin
    from urllib import quote_plus
    from urllib2 import urlopen, unquote
    from HTMLParser import HTMLParser
    input = raw_input
    str = unicode
    range = xrange

from pyquery import PyQuery

from pyfetcher import extractors
from pyfetcher.crawlers.common import BaseCrawler
from pyfetcher.items import Media, Stream
from pyfetcher.utils import async


class TubeplusCrawler(BaseCrawler):

    def __init__(self):
        super(TubeplusCrawler, self).__init__()  # to be ported
        self.description = "Crawler for the tubeplus streaming site"
        self.site_url = "http://www.tubeplus.me/"

    def get_streams(self, media):
        logging.info("Extracting: {}".format(media))

        if not media.url:
            logging.warn("{} has no url".format(media))
            return None

        media_page = self.fetch_page(media.url)
        pq = PyQuery(media_page)

        stream_list = []

        # extract video id and video host name from href links
        # from page fetched by media url
        href_rgx = re.compile(
            r"'(?P<vid>[\w\.:/\?\=\&]+)'[\s,]+'(?:[\w\s\-\":,\.`´\\]+)?'[\s,]+'(?P<host>[\w\.]+)'"
        )
        for href in (a.attrib.get('href') for a in pq('#links_list .link a:not([class])')):
            try:
                video_url = href
                video_host = href_rgx.search(href).group('host')
                video_id = href_rgx.search(href).group('vid')

                stream = Stream(video_id, video_host, video_url)
                logging.info("Found {} for {}".format(stream, media))

                stream_list.append(stream)
            except AttributeError:
                # if an exception occured the href_rgx couldn't match something on href
                logging.error("Couldn't get video info from: {}".format(href))
                pass

        return stream_list

    def get_children(self, media):
        logging.info('Searching children for media: {}'.format(media.verbose_name))

        media_page = self.fetch_page(media.url)
        pq = PyQuery(media_page)

        rgx = re.compile(
            r"/player/\d+/(?P<serie>\w+)/season_(?P<season>\d+)/episode_(?P<episode>\d+)/(?P<title>[\w´`\'\",\.]+)")
        links = [a.attrib.get('href') for a in pq('.seasons[href]')]

        # build episodes
        episode_list = []
        for link in links:

            title = re.search(rgx, link).group('title')
            title = re.sub('_', ' ', title)
            category = "Tv Show Episode"
            url = urljoin(self.site_url, link)

            episode = Media(name=title, category=category, url=url)

            link = HTMLParser().unescape(unquote(link))
            episode.episode_num = int(re.search(rgx, link).group('episode'))
            episode.season_num = int(re.search(rgx, link).group('season'))

            episode_list.append(episode)

        return episode_list

    def search_tvshow(self, search_query):
        logging.info('Searching tvshow for query: {}'.format(search_query))

        search_url = urljoin(self.site_url, "/search/tv-shows/")
        search_url = urljoin(search_url, quote_plus(search_query))

        logging.info("url search: {}".format(search_url))

        search_page = self.fetch_page(search_url)
        pq = PyQuery(search_page)

        dom_search_list = pq(u".list_item")
        tvshow_list = []

        for dom_item in dom_search_list:
            title = pq(dom_item).find('img[border="0"]').show().attr('alt')
            category = "Tv Show"
            tvshow = Media(name=title, category=category)

            # Since it is a tvshow we need to fetch the children episodes
            tvshow.has_children = True

            # set description
            desc = pq(dom_item).find('.plot').text()
            tvshow.description = re.sub('\s', ' ', str(desc))  # remove newlines from description

            # set rating
            tvshow.rating = pq(dom_item).find('span.rank_value').text()

            # set page url
            href = pq(dom_item).find('a.panel').attr('href')
            tvshow.url = urljoin(self.site_url, href)

            # set thumbnail url
            href_thumbnail = pq(dom_item).find('img[border="0"]').show().attr('src')
            tvshow.thumbnail = urljoin(self.site_url, href_thumbnail)

            # logging.info(tvshow)

            tvshow_list.append(tvshow)

        return tvshow_list

    def search_film(self, search_query):
        logging.info('Searching film for query: {}'.format(search_query))

        search_url = urljoin(self.site_url, "/search/movies/")
        search_url = urljoin(search_url, quote_plus(search_query))

        search_page = self.fetch_page(search_url)
        pq = PyQuery(search_page)

        dom_search_list = pq(u".list_item")
        film_list = []
        for dom_item in dom_search_list:
            name = pq(dom_item).find('img[border="0"]').show().attr('alt')
            category = "Film"

            film = Media(name=name, category=category)

            # set description
            desc = pq(dom_item).find('.plot').text()
            film.description = re.sub('\s', ' ', str(desc))  # remove newlines from description

            film.rating = pq(dom_item).find('span.rank_value').text()

            # set page url
            href = pq(dom_item).find('a.panel').attr('href')
            film.url = urljoin(self.site_url, href)

            # set thumbnail url
            href_thumbnail = pq(dom_item).find('img[border="0"]').show().attr('src')
            film.thumbnail = urljoin(self.site_url, href_thumbnail)

            film_list.append(film)

        return film_list

    def search(self, search_query):
        """ Return a list of Media objects found by search_query
        """
        film_list = self.search_film(search_query)
        serie_list = self.search_tvshow(search_query)

        return film_list + serie_list
