# Building a crawler step by step

## Create a file and drop it in the "crawlers directory"

Convention is to create a file named starting with "crawler_"

```
touch pyfetcher/crawlers/crawler_example
```

## Crawler example

The crawler class should be named finishing with "Crawler" and be a subclass of BaseCrawler.

File: crawler_example.py

```python

from pyfetcher import extractors
from pyfetcher.crawlers.common import BaseCrawler
from pyfetcher.items import Media, Stream
from pyfetcher.utils import async

class ExampleCrawler(BaseCrawler):

    def __init__(self):
        # default site url
        self.site_url = "http://www.example.com"

    # return a list of stream for given media            
    get_streams(self, media):
        pass
        
    # return a list of Media for given media
    get_children(self, media):
        pass
        
    # return a list of Media for given search query
    search(self, search_query):
        pass        
```