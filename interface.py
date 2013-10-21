#!/usr/bin/env python
# -*- coding: utf-8 -*-
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

    def search_menu(choices):
        pass

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
            search_series = Console.crawler.search_serie(query)

    @staticmethod
    def run():
        try:
            while True:
                Console.main_menu()
        except KeyboardInterrupt:
            print('')
            pass
