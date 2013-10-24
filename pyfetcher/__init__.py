import argparse
import logging

import crawlers
import interface


def get_crawler_list():
    crawler_list = crawlers.get_all_crawlers()
    return '\n'.join("> " + c.name for c in crawler_list)


def main():
    aparser = argparse.ArgumentParser()
    aparser.add_argument("-o", "--output_file", help="Output file name")
    aparser.add_argument("-v", "--verbose", action="store_true", help="verbose output")
    aparser.add_argument(
        "-c", "--crawler", default="tubeplus",
        help="Crawler name (example: -c streamsite)\n" + get_crawler_list()
    )
    args = aparser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)

    if args.crawler:
        crawler_name = args.crawler
        crawler = crawlers.get_crawler(name=crawler_name)

        output_file = args.output_file
        interface.Console.run(crawler, output_file=output_file)
