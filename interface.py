# -*- coding: utf-8 -*-
import sys
try:
    from urllib2 import urlopen, Request
    input = raw_input
    str = unicode
    range = xrange
except:
    pass

from crawlers import TubeplusCrawler


class Console(object):

    crawler = TubeplusCrawler()

    @staticmethod
    def prompt(choices=None):
        if choices:
            for i, item in enumerate(choices):
                if isinstance(item, tuple) and len(item) > 1:
                    print(u"[{0}] {1}".format(item[0], item[1]))
                else:
                    print(u"[{0}] {1}".format(i, item))
        choice = input('>>> ')
        return choice

    @staticmethod
    def series_menu(series):
        choice = Console.prompt(s.name for s in series)
        try:
            idx = int(choice)
            serie_chosen = series[idx] if len(series) > idx else None
            if serie_chosen:
                episodes = Console.crawler.get_seasons(serie=serie_chosen)
        except ValueError:
            sys.stderr.write('ERREUR: tapez un numero')

    @staticmethod
    def main_menu():
        search_options = ['Film', 'Serie']
        choice = Console.prompt(choices=search_options)
        if choice == '0':
            print("Search film is not implemented")
            # query = Console.prompt()
            # Console.crawler.search_film(query)
        elif choice == '1':
            print("Rechercher serie par nom (CTRL-C pour quitter): ")
            query = Console.prompt()
            found_series = Console.crawler.search_serie(query)
            Console.series_menu(found_series)

    @staticmethod
    def run():
        try:
            while True:
                Console.main_menu()
        except KeyboardInterrupt:
            print('')
            pass
