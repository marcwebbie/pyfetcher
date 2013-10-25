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
from pyfetcher.crawlers.common import BaseCrawler, Search
from pyfetcher.items import Media
from pyfetcher.utils import async


class TubeplusCrawler(BaseCrawler):

    def __init__(self):
        super(TubeplusCrawler, self).__init__()  # to be ported
        self.name = "tubeplus"
        self.description = "Crawler for the tubeplus streaming site"
        self.site_url = "http://www.tubeplus.me/"

    def extract(self, media, show_progress=True):
        media_page = self.fetch_page(media.url)
        pq = PyQuery(media_page)

        url_list = []

        # extract video_id and hostname from links and extract url
        href_rgx = re.compile(
            r"'(?P<vid>[\w\.:/\?\=\&]+)'[\s,]+'(?:[\w\s\-\":,\.`´\\]+)?'[\s,]+'(?P<host>[\w\.]+)'"
        )
        for href in (a.attrib.get('href') for a in pq('#links_list .link a:not([class])')):
            try:
                video_host = href_rgx.search(href).group('host')
                video_id = href_rgx.search(href).group('vid')
                extor = extractors.get_by_hostname(video_host)

                if extor:
                    dl_url = extor.raw_url(video_id)
                    if dl_url:
                        url_list.append(dl_url)
                        logging.info("Found download url: {}".format(dl_url))

                    if show_progress:
                        # update user. '.' means success, 'F' means not fetched url
                        sys.stdout.write('.' if dl_url else 'F')
                        sys.stdout.flush()
            except AttributeError:
                # if an exception occured the regex couldn't match something
                logging.error("Couldn't get video info from: {}".format(href))

        if show_progress:
            print('')
        return url_list

    def get_children(self, media):
        """
        Get a children for a given media

        media (Media) -> Media object to search for children
        """

        logging.info('Searching children for media: {}'.format(media.verbose_name))

        media_page = self.fetch_page(media.url)
        pq = PyQuery(media_page)

        rgx = re.compile(
            r"/player/\d+/(?P<serie>\w+)/season_(?P<season>\d+)/episode_(?P<episode>\d+)/(?P<title>[\w´`\'\",\.]+)")
        links = [a.attrib.get('href') for a in pq('.seasons[href]')]

        # build episodes
        episodes = []
        for link in links:

            title = re.search(rgx, link).group('title')
            title = re.sub('_', ' ', title)
            category = "Tv Show Episode"

            episode = Media(name=title, category=category)

            episode.url = urljoin(self.site_url, link)

            link = HTMLParser().unescape(unquote(link))
            episode.episode_num = int(re.search(rgx, link).group('episode'))
            episode.season_num = int(re.search(rgx, link).group('season'))

            # imdb_url = pq(".imdb").attr('href')
            # logging.info('imdb url for {}: {}'.format(episode.verbose_name, imdb_url))

            # if imdb_url:
            #     imdb_page = self.fetch_page(imdb_url)
            #     pq_rating = PyQuery(imdb_page)

            #     rating = pq_rating('span[itemprop=ratingValue]').text()
            #     logging.info('imdb rating for {}: {}'.format(episode.verbose_name, rating))
            #     episode.rating = rating + "/10" if rating else None

            episodes.append(episode)

        return episodes

    def search_tvshow(self, search_query):
        """Return a list of Media objects found by search_query"""

        logging.info('Searching tvshow: {}'.format(search_query))

        search_url = urljoin(self.site_url, "/search/tv-shows/")
        search_url = urljoin(search_url, quote_plus(search_query))

        logging.info("url search: {}".format(search_url))

        search_page = self.fetch_page(search_url)
        pq = PyQuery(search_page)

        dom_search_list = pq(u".list_item")
        tvshow_list = []
        for dom_item in dom_search_list:

            # set title
            name = pq(dom_item).find('img[border="0"]').show().attr('alt')

            # add category
            category = "Tv Show"

            tvshow = Media(name=name, category=category)

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

            logging.info(tvshow)

            tvshow_list.append(tvshow)

        return tvshow_list

    def search_film(self, search_query):
        """Return a list of Media objects found by search_query"""

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
            film.retrieved_url = urljoin(self.site_url, href)

            # set thumbnail url
            href_thumbnail = pq(dom_item).find('img[border="0"]').show().attr('src')
            film.thumbnail = urljoin(self.site_url, href_thumbnail)

            film_list.append(film)

        return film_list

    def search(self, search_query):
        film_list = self.search_film(search_query)
        serie_list = self.search_tvshow(search_query)

        return film_list + serie_list


    # @staticmethod
    # def prompt(choices=None, enum_choices=True):
    #     if choices:
    #         try:
    #             if enum_choices:
    #                 for i, item in enumerate(choices):
    #                     print(u"[{0}] {1}".format(i, item))
    #             else:
    #                 for item in choices:
    #                     print(item)
    #         except TypeError:
    #             sys.stderr.write("ERROR: choices isn't iterable")
    #             pass

    #     choice = input('Input: ')
    #     return choice

    # @staticmethod
    # def get_episode_urls(episode):
    #     url_list = Interface.crawler.get_episode_raw_urls(episode)
    #     if url_list:
    #         for url in url_list:
    #             print(url)

    # help message
    #         print('')
    #         print('====================================')
    #         print('Télécharger fichier avec cURL example:')
    #         print('  curl -o <nom_du_fichier.mp4> http://address.du.serveur.com/video.mp4')
    #         print('====================================')

    # @staticmethod
    # def series_menu(series):
    #     choice = Interface.prompt(u"{} [note: {}]".format(s.name, s.rating) for s in series)
    #     try:
    #         idx = int(choice)
    #     except ValueError:
    #         sys.stderr.write(u'ERREUR: tapez un numero\n')
    #         return None

    #     serie_chosen = series[idx] if len(series) > idx else None
    #     if serie_chosen:
    #         seasons = Interface.crawler.get_seasons(serie=serie_chosen)
    #         serie_chosen.extend_seasons(seasons)

    # build episode choice list
    #         choice_list = []
    #         for season in serie_chosen.seasons:
    #             choice_list.append(season.verbose_name)
    #             choice_list.extend(
    #                 u"  [{0}] {1}".format(e.code, e.name) for e in season.episodes
    #             )

    #         episode_chosen_cod = Interface.prompt(choice_list, enum_choices=False)

    #         if serie_chosen.get_episode(episode_chosen_cod):
    #             chosen_episode = serie_chosen.get_episode(episode_chosen_cod)
    #             Interface.get_episode_urls(chosen_episode)

    # @staticmethod
    # def films_menu(film_list):
    #     fchoice = Interface.prompt(u"{} [note: {}]".format(film.name, film.rating)
    #                                for film in film_list)
    #     try:
    #         idx = int(fchoice)
    #         film_chosen = film_list[idx]
    #     except ValueError:
    #         sys.stderr.write(u'ERREUR: tapez un numero\n')
    #         return None

    #     url_list = Interface.crawler.get_episode_raw_urls(film_chosen)
    #     if url_list:
    #         for url in url_list:
    #             print(url)

    # help message
    #         print('')
    #         print('====================================')
    #         print('Télécharger fichier avec cURL example:')
    #         print('  curl -c <nom_du_fichier.mp4> http://address.du.serveur.com/video.mp4')
    #         print('====================================')
    #     else:
    #         print("Ce film n'a pas d'url disponible")

    # @staticmethod
    # def main_menu():
    #     print("")
    #     print(u"Tapez le code (ex: 0) d'interface (CTRL-C pour quitter): ")
    #     search_options = [u'Film', u'Serie']
    #     choice = Interface.prompt(choices=search_options)
    #     if choice == '0':
    #         print(u"Rechercher film par nom: ")
    #         query = Interface.prompt()
    #         found_films = Interface.crawler.search_film(query)
    #         Interface.films_menu(found_films)
    #     elif choice == '1':
    #         print(u"Rechercher serie par nom: ")
    #         query = Interface.prompt()
    #         found_series = Interface.crawler.search_serie(query)
    #         Interface.series_menu(found_series)

    # @staticmethod
    # def run():
    #     try:
    #         while True:
    #             Interface.main_menu()
    #     except KeyboardInterrupt:
    #         print('')
    #         pass
