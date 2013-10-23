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
    def prompt(choices=None, enum_choices=True):
        if choices:
            try:
                if enum_choices:
                    for i, item in enumerate(choices):
                        print(u"[{0}] {1}".format(i, item))
                else:
                    for item in choices:
                        print(item)
            except TypeError:
                sys.stderr.write("ERROR: choices isn't iterable")
                pass

        choice = input('Input: ')
        return choice

    @staticmethod
    def get_episode_urls(episode):
        url_list = Console.crawler.get_episode_raw_urls(episode)
        if url_list:
            for url in url_list:
                print(url)

            # help message
            print('')
            print('====================================')
            print('Télécharger fichier avec cURL example:')
            print('  curl -o <nom_du_fichier.mp4> http://address.du.serveur.com/video.mp4')
            print('====================================')

    @staticmethod
    def series_menu(series):
        choice = Console.prompt(u"{} [note: {}]".format(s.name, s.rating) for s in series)
        try:
            idx = int(choice)
        except ValueError:
            sys.stderr.write(u'ERREUR: tapez un numero\n')
            return None

        serie_chosen = series[idx] if len(series) > idx else None
        if serie_chosen:
            seasons = Console.crawler.get_seasons(serie=serie_chosen)
            serie_chosen.extend_seasons(seasons)

            # build episode choice list
            choice_list = []
            for season in serie_chosen.seasons:
                choice_list.append(season.verbose_name)
                choice_list.extend(
                    u"  [{0}] {1}".format(e.code, e.name) for e in season.episodes
                )

            episode_chosen_cod = Console.prompt(choice_list, enum_choices=False)

            if serie_chosen.get_episode(episode_chosen_cod):
                chosen_episode = serie_chosen.get_episode(episode_chosen_cod)
                Console.get_episode_urls(chosen_episode)

    @staticmethod
    def films_menu(film_list):
        fchoice = Console.prompt(u"{} [note: {}]".format(film.name, film.rating)
                                 for film in film_list)
        try:
            idx = int(fchoice)
            film_chosen = film_list[idx]
        except ValueError:
            sys.stderr.write(u'ERREUR: tapez un numero\n')
            return None

        url_list = Console.crawler.get_episode_raw_urls(film_chosen)
        if url_list:
            for url in url_list:
                print(url)

            # help message
            print('')
            print('====================================')
            print('Télécharger fichier avec cURL example:')
            print('  curl -c <nom_du_fichier.mp4> http://address.du.serveur.com/video.mp4')
            print('====================================')
        else:
            print("Ce film n'a pas d'url disponible")

    @staticmethod
    def main_menu():
        print("")
        print(u"Tapez le code (ex: 0) d'interface (CTRL-C pour quitter): ")
        search_options = [u'Film', u'Serie']
        choice = Console.prompt(choices=search_options)
        if choice == '0':
            print(u"Rechercher film par nom: ")
            query = Console.prompt()
            found_films = Console.crawler.search_film(query)
            Console.films_menu(found_films)
        elif choice == '1':
            print(u"Rechercher serie par nom: ")
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
