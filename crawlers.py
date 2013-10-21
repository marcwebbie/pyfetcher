
from items import Film, Serie, Season, Episode


class BaseCrawler(object):

    def __init__(self):
        self.name = None


class TubeplusCrawler(BaseCrawler):

    def __init__(self):
        super(TubeplusCrawler, self).__init__()  # to be ported

    def search_serie(self, search_query):
        print("Search serie is not implemented")
        # search_query = input("Rechercher serie par nom (CTRL-C pour quitter): ")
        # print(u"En recherche de '{}'...".format(search_query))

        # search_result_list = cls.search(search_query)
        # rgx = re.compile(r'Watch online: ')
        # clean_list = [re.sub(rgx, '', a.get('title')) for a in search_result_list]
        # selected_index = cls.select_item(
        #     clean_list, prompt="Tapez num série (CTRL-C pour quitter): ")
        # serie_url = search_result_list[selected_index].attrib['href']
        # cls.serie_page(serie_url)

    def search_film(self, search_query):
        print("Search film is not implemented")
