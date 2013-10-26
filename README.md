# PyFetcher

PyFetcher is tool to crawl stream sites extract download links.

## To install type:

```bash
pip install https://bitbucket.org/marcwebbie/pyfetcher/get/master.tar.gz
```


## To reinstall type:

```bash
pip install -U https://bitbucket.org/marcwebbie/pyfetcher/get/master.tar.gz
```


## To remove type:

```bash
pip uninstall pyfetcher
```


# Quick start

## Crawl the with default streamsite crawler:

```bash
pyfetcher
```


## Check the list of available crawlers:

```bash
pyfetcher -lc all
```


## Crawl with an specific crawler:

```bash
pyfetcher -c <crawler_name>
```


## Crawn and save urllist to a file

```bash
pyfetcher -o <output_filename>
```


## Crawn and return urllist as json

```bash
pyfetcher -j
```


## Crawn and save urllist as json to a file

```bash
pyfetcher -j -o
```

# As a library

PyFetcher can be used as a library to fetch stream lists.


## PyFetcher objects

### Media: 

Holds media information normally extracted from site page for a given video

```python
class Media(object):

    def __init__(self, name, category):

        self.name = name
        self.category = category
        self.url = None

        # additional metadata
        self.description = None
        self.season_num = None
        self.episode_num = None
        self.has_children = None
        self.rating = None
        self.year = None
        self.thumbnail = None
        self.director = None
        self.actors = []

    @property
    def verbose_name(self):

    @property
    def code(self):

    def __repr__(self):
```

### Stream: 

Contain the direct stream info. those are build by crawler.extract using info extractors

```python
class Stream(object):
    self.id
    self.host 
    self.url
```


## Examples:

### Fetch stream pages from a given stream search page.

The info:

+ Stream search page: http://www.example.com/videos

+ Stream search page crawler: "example"

+ Video to search: "The Hunt for Gollum"

```python
from pyfetchern import crawlers

crawler_name = "example"
crawler = crawlers.get_crawler(name=crawler_name)

film_name = "The Hunt for Gollum"
search_query = film_name

# Search the film, crawler.search returns a list of Media objects
found_medias = crawler.search(search_query)

# get the first media and extract extract its streams
stream_list = crawler.extract(found_medias[0])

# print all urls
for stream in stream_list:
    print("{0}: {1}".format(stream.host, stream.url))
``` 

Result:

```bash
youtube: http://www.youtube.com/watch?v=GGgjrwzkWMA
dailymotion: http://www.dailymotion.com/video/x93zji_the-hunt-for-gollum-hd-version_shortfilms
``` 


## Licence ([GPLv3 License](http://opensource.org/licenses/GPL-3.0))

Copyright (C) 2013 [Marcwebbie](https://bitbucket.org/marcwebbie)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.