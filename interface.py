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
                if isinstance(item, (tuple, list)) and len(item) > 1:
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
                seasons = Console.crawler.get_seasons(serie=serie_chosen)
                import pdb
                pdb.set_trace()

                # build episode choice list
                choice_list = []
                for season in seasons:
                    choice_list.append(u"Season {0}".format(season.number))
                    choice_list.extend(u"  [{}] {}".format(e.code, e.name) for e in season.episodes)
                Console.prompt(choice_list)

        except ValueError:
            sys.stderr.write(u'ERREUR: tapez un numero')

    @staticmethod
    def main_menu():
        search_options = [u'Film', u'Serie']
        choice = Console.prompt(choices=search_options)
        if choice == '0':
            print(u"Rechercher film par nom (CTRL-C pour quitter): ")
            query = Console.prompt()
            Console.crawler.search_film(query)
        elif choice == '1':
            print(u"Rechercher serie par nom (CTRL-C pour quitter): ")
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
