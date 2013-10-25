import argparse
import logging

import crawlers
import interface


def get_crawler_list():
    crawler_list = crawlers.get_all_crawlers()
    return (c.name for c in crawler_list)


def get_args():
    aparser = argparse.ArgumentParser()
    aparser.add_argument("-j", "--json", help="Output extract url as JSON")
    aparser.add_argument("-o", "--output_file", action="store_true", help="Output file name")
    aparser.add_argument("-v", "--verbose", action="store_true", help="verbose output")
    aparser.add_argument(
        "-lc", "--list_crawler", action="store_true", help="Print a list of available crawlers")
    aparser.add_argument(
        "-c", "--crawler", default="tubeplus",
        help="Crawler name (example: -c streamsite)"
    )
    args = aparser.parse_args()
    return args


def main():
    args = get_args()

    if args.list_crawler:
        print("Available crawlers")
        print("=============================")
        crawler_list = get_crawler_list()
        print("\n".join(crawler_list))
        print("")
        return  # exit

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)

    if args.crawler:
        crawler_name = args.crawler
        crawler = crawlers.get_crawler(name=crawler_name)

        output_file = args.output_file
        interface.Console.run(crawler, output_file=output_file)
