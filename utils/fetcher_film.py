import re
import sys
from urllib.request import urlopen
from pyquery import PyQuery as pq

url = 'http://www.tubeplus.me/'


class GorillaVidExtractor:
    host_list = ["gorillavid", "gorillavid.in"]
    holder_url = "http://gorillavid.in/embed-{}-650x400.html"

    @classmethod
    def is_valid_host(cls, host):
        return host in cls.host_list

    @classmethod
    def raw_url(cls, video_id):
        dest_url = cls.holder_url.format(video_id)
        html_embed = str(urlopen(dest_url).read())
        found = re.findall(r'(http://[\w\./0-9:]+\.(?:mp4|flv))', html_embed)

        if found:
            return found[0]


class VidBullExtractor:
    host_list = ["vidbull.com"]
    holder_url = "http://vidbull.com/embed-{}-650x328.html"

    @classmethod
    def is_valid_host(cls, host):
        return host in cls.host_list

    @classmethod
    def raw_url(cls, video_id):
        dest_url = cls.holder_url.format(video_id)
        html_embed = str(urlopen(dest_url).read())
        found = re.findall(r'(http://[\w\./0-9:]+\.(?:mp4|flv))', html_embed)

        # raw_url_list = []
        if found:
            # sys.stderr.write("  {}\n".format(found[0]))
            return found[0]
            # raw_url_list.append(found)


class Episode:

    def __init__(self, node):
        self.id = node.attrib.get('id')
        self.title = node.text
        self.href = node.attrib.get('href')
        self.season = re.match(r's(\d+)', self.id).group(1)


def get_raw_url(href):
    html_ep = urlopen("{}{}".format(url, href)).read()
    d = pq(html_ep)

    raw_url_list = []
    link_list = [a for a in d('.online .link a') if 'javascript:show' in a.attrib.get('href')]
    for link in link_list:
        href_args = re.findall(r"'([\w\s0-9\.\-_:]+)'", link.attrib.get('href'))
        # print(href_args)

        if GorillaVidExtractor.is_valid_host(href_args[-1]):
            sys.stdout.write('.')
            sys.stdout.flush()
            found_url = GorillaVidExtractor.raw_url(href_args[0])
            if found_url:
                raw_url_list.append(found_url)

        if VidBullExtractor.is_valid_host(href_args[-1]):
            sys.stdout.write('.')
            sys.stdout.flush()
            found_url = GorillaVidExtractor.raw_url(href_args[0])
            if found_url:
                raw_url_list.append(found_url)

    # print list of raw urls to be copied
    print('')
    print('-----------------------------------')
    for raw in set(raw_url_list):
        print(raw)
    print('-----------------------------------')


def serie_menu(url_serie):
    html_serie = urlopen("{}{}".format(url, url_serie)).read()
    d = pq(html_serie)
    episodes = []
    for node in d('.parts a'):
        season_num = re.match(r's(\d+)', node.attrib.get('id')).group(1)
        episodes.append(Episode(node))

    for season in sorted(set([e.season for e in episodes])):
        print("Season:", season)
        for episode in [e for e in episodes if e.season == season]:
            print("  [{}] {}".format(episode.id, episode.title))

    cod_episode = input("Tapez le code (ex: s1e1) episode (CTRL-C pour quitter): ")
    found_episodes = [e for e in episodes if e.id == cod_episode]
    ep = found_episodes[0] if found_episodes else None

    if ep:
        # print("href:", ep.href)
        get_raw_url(ep.href)


def main_menu():
    while True:
        search_query = input("Rechercher serie par nom (CTRL-C pour quitter): ")
        search_url = "{}search/tv-shows/{}".format(
            url, search_query.replace(' ', '+'))
        # print('URL:', search_url)
        print("En recherche de '{}'...".format(search_query))
        # import pdb
        # pdb.set_trace()
        html_search_result = urlopen(search_url).read()

        d = pq(html_search_result)
        search_result_list = d("#list_body .list_item .left a")
        for pos, a in enumerate(search_result_list):
            title = re.sub('Watch online: ', '', a.get('title'))
            print("[{}] {}".format(pos, title))

        if search_result_list:
            serie = 0
            while True:
                try:
                    num_serie = int(input("Tapez num série (CTRL-C pour quitter): "))
                    serie = search_result_list[num_serie]
                    break
                except ValueError:
                    print('ERREUR: tapez un numero entre 1 et {}'.format(len(search_result_list)))
                    print("%s -> %s" % (serie.get('title'), serie_url))

            serie_url = serie.attrib['href']
            serie_menu(serie_url)


if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print('')
        pass
