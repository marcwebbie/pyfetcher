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

from pyquery import PyQuery as pq

DEBUG = False


class BaseExtractor:

    def __init__(self):
        self.host_list = []
        self.std_headers = {
            'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'}

    def is_valid_host(self, host):
        return host in self.host_list

    def is_valid_url(self):
        pass


class GorillaVidExtractor(BaseExtractor):

    def __init__(self):
        self.host_list = ["gorillavid", "gorillavid.in"]
        self.holder_url = "http://gorillavid.in/embed-{}-650x400.html"
        self.regex_url = None

    def raw_url(self, video_id):
        dest_url = self.holder_url.format(video_id)
        html_embed = str(urlopen(dest_url).read())
        found = re.findall(r'(http://[\w\./0-9:]+\.(?:mp4|flv))', html_embed)

        if found:
            return found[0]

    def is_valid_url(self):
        pass


class VidbullExtractor(BaseExtractor):

    def __init__(self):
        self.host_list = ["vidbull.com"]
        self.holder_url = "http://vidbull.com/embed-{}-650x328.html"
        self.regex_url = None

    @staticmethod
    def baseconv(number, base=36):
        alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
        result = ''
        while number:
            number, i = divmod(number, base)
            result = alphabet[i] + result

        return result or alphabet[0]

    @staticmethod
    def unpacker(p, a, c, k, e=None, d=None):
        for c in reversed(range(c)):
            if(k[c]):
                p = re.sub(r'\b' + VidbullExtractor.baseconv(c, base=a) + r'\b', k[c], p)
        return p

    def raw_url(self, video_id):
        dest_url = self.holder_url.format(video_id)
        html_embed = str(urlopen(dest_url).read())

        # get script with the packed eval function
        d = pq(html_embed)
        script_text_raw = d('#player_code script:not([src])').text()
        script_text = re.sub(r'\\', '', str(script_text_raw))

        rgx = re.compile(r"}\('(.+)',(\d+),(\d+),'([\w|]+)'")

        try:
            parg1 = re.search(rgx, script_text).group(1)
            parg2 = int(re.search(rgx, script_text).group(2))
            parg3 = int(re.search(rgx, script_text).group(3))
            parg4 = re.search(rgx, script_text).group(4).split('|')
        except:
            if DEBUG:
                print('ERROR trying to parse script text')
            return None
        try:
            unpacked_vars = self.unpacker(parg1, parg2, parg3, parg4)
        except:
            if DEBUG:
                print('ERROR trying unpack script text')
            return None
        try:
            raw = re.search(r'file:"([\w\.:/\-_]+)"', unpacked_vars).group(1)
        except:
            if DEBUG:
                print('ERROR file raw url not found in script unpacked')
            return None

        return raw

    def is_valid_url(self):
        pass


EXTRACTOR_INSTANCES = [
    GorillaVidExtractor(),
    VidbullExtractor()
]


def get_instances():
    return EXTRACTOR_INSTANCES


def get_by_url(url):
    for extractor in get_instances():
        if extractor.is_valid_url(url):
            return extractor


def get_by_hostname(hostname):
    for extractor in get_instances():
        if extractor.is_valid_host(hostname):
            return extractor
