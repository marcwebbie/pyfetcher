import logging
import os
import sys
import unittest

test_path = os.path.realpath(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(test_path)))

from pyfetcher import crawlers
from pyfetcher import extractors
from pyfetcher import items


class CrawlersTestCase(unittest.TestCase):

    def test_general(self):

        crawler = crawlers.get_crawler(name='tubeplus')

        medialist = crawler.search_film('Eat pray love')

        media = medialist[0]

        stream_list = crawler.get_streams(media)

        for stream in stream_list:
            extractor = extractors.get_by_hostname(stream.host)
            download_url = None

            if extractor:
                download_url = extractor.raw_url(stream.sid)

            print(stream)
            print("└── Extractor = {}".format(extractor))
            print("└── Url = {}".format(download_url))

    def test_crawler_search_return_media_list(self):
        crawler_list = crawlers.get_all_crawlers()

        self.assertNotEqual(crawler_list, None)
        self.assertIsInstance(crawler_list, list)
        self.assertGreater(len(crawler_list), 0)

        first_crawler = crawler_list[0]

        search_result = first_crawler.search("")

        for result in search_result:
            self.assertIsInstance(result, items.Media)

if __name__ == "__main__":
    unittest.main()
