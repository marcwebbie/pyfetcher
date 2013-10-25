# -*- coding: utf-8 -*-
import logging

try:
    input = raw_input
except NameError:
    pass


class Console(object):

    @staticmethod
    def prompt(choice_list=None, text='Input: '):
        """ Open prompt for input """

        if not choice_list:
            return input(text)

        # print choices
        try:
            for idx, media in enumerate(choice_list):
                fstr = u"[{0}] {1}"
                if media.code:
                    line = fstr.format(media.code, media.name)
                else:
                    line = fstr.format(idx, media.name)

                category = media.category
                rating = media.rating
                info = "[{0}, Rating: {1}]".format(category, rating)

                # padding extra info
                pad_size = 100
                info_padded = "{0:>{1}}".format(info, pad_size - len(line))
                print(line + info_padded)
        except TypeError:
            logging.error("ERROR: choices isn't iterable")
            pass

        # ask for input
        choice = input(text)

        # select a choice
        media_chosen = None
        try:
            # try indexing
            media_chosen = choice_list[int(choice)]
        except (IndexError, ValueError):
            # try by code
            for media in (m for m in choice_list if m.code == choice):
                # found at least one media with choice code
                media_chosen = media

        return media_chosen

    @staticmethod
    def get_streams(crawler, media):
        stream_list = crawler.extract(media)

        if not stream_list:
            logging.info(
                "Couldn't find streams for media: {}".format(media)
            )

        return stream_list

    @staticmethod
    def search(crawler):
        query = Console.prompt(
            choice_list=None, text=u"Rechercher stream par nom (Ctrl-C pour quitter): ")

        search_result = crawler.search(query)

        if search_result:
            media_chosen = Console.prompt(choice_list=search_result)

            if media_chosen:
                while media_chosen.has_children:
                    logging.info("Chosen media has children: {}".format(media_chosen))
                    children = crawler.get_children(media_chosen)
                    media_chosen = Console.prompt(choice_list=children)

                    if not media_chosen:
                        return None

                stream_list = Console.get_streams(crawler, media_chosen)
                return stream_list

    @staticmethod
    def get_url_list(stream_list, show_progress=False):
        from pyfetcher import extractors

        url_list = []
        for stream in stream_list:
            extractor = extractors.get_by_hostname(stream.host)

            if extractor:
                download_url = extractor.raw_url(stream.sid)

                if download_url:
                    url_list.append(download_url)

        return url_list

    @staticmethod
    def run(crawler, output_file=None, repeat=False):
        while True:
            show_progress = True if output_file else False
            stream_list = Console.search(crawler)

            if stream_list:
                logging.info('Extracted streams count: {}'.format(len(stream_list)))

                url_list = Console.get_url_list(stream_list, show_progress)

                if output_file and url_list:
                    with open(output_file, 'w') as out_f:
                        out_f.write('\n'.join(url_list))
                elif url_list:
                    print('')
                    print('\n'.join(url_list))
                    print('')
                    print('====================================')
                    print('Télécharger fichier avec cURL example:')
                    print('  curl -o <nom_du_fichier.mp4> http://address.du.serveur.com/video.mp4')
                    print('====================================')
                else:
                    return None

            if not repeat:
                break
