# -*- coding: utf-8 -*-
import re
import sys
try:
    from urllib.request import urlopen, Request
    from urllib.parse import unquote, urlencode
    from html.parser import HTMLParser
except:
    from urllib import urlencode
    from urllib2 import urlopen, Request, unquote
    from HTMLParser import HTMLParser
    input = raw_input
    str = unicode
    range = xrange

from pyquery import PyQuery

from pyfetcher.utils import WiseUnpacker
import logging


class BaseExtractor(object):

    def __init__(self):
        self.std_headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0'}

    def fetch_page(self, url):
        headers = self.std_headers
        req = Request(url, data=None, headers=headers)
        response = urlopen(req)
        the_page = response.read()
        return the_page

    def is_valid_host(self, host):
        return host in self.host_list

    def is_valid_url(self):
        pass

    @property
    def name(self):
        return self.__class__.__name__.lower()

    def __str__(self):
        s = "{0}(name={1}, host_list={2})".format(
            self.__class__.__name__,
            self.name,
            self.host_list
        )

        return s


class NowVideoExtractor(BaseExtractor):

    """
    Wireshark capturing: url(http://embed.nowvideo.sx/embed.php?v=hanu11wjzx2d7&width=650&height=510)
    192.168.42.124  185.7.35.135    HTTP    582 GET /api/player.api.php?cid3=undefined&pass=undefined&key=177%2E206%2E184%2E253%2D36f6376e4d8bfedb4b4e28baf4393f43&user=undefined&numOfErrors=0&cid=undefined&file=hanu11wjzx2d7&cid2=undefined HTTP/1.1 
    192.168.42.124  78.152.42.242   HTTP    492 GET /dl/462b0da6ffb49dca14b86ea264054ba7/52660927/ff43ca5c13c8fbceae5af4f2a863a5f8e0.flv?client=FLASH HTTP/1.1 
    
    script with info:

        <!-- For version detection, set to min. required Flash Player version, or 0 (or 0.0.0), for no version detection. --> 

        var swfVersionStr = "10.0.0";
            
        function logout(){
            
            document.getElementById('mis').innerHTML ='<iframe frameborder="0" width="1"  height="1" scrolling="0"  src="http://www.nowvideo.sx/api/embed.logger.php?logout=1">';
            document.getElementById('mis2').innerHTML ='<iframe frameborder="0" width="1"  height="1" scrolling="0"  src="/logger.php?logout=1">';
        }

        function disableAds(x,y,z) {
        
        document.getElementById('mis').innerHTML ='<iframe frameborder="0" width="1"  height="1" scrolling="0"  src="http://www.nowvideo.sx/api/embed.logger.php?user='+x+'&pass='+y+'">';
        document.getElementById('mis2').innerHTML ='<iframe frameborder="0" width="1"  height="1" scrolling="0"  src="/logger.php?user='+x+'&pass='+y+'">';
        if(z>0){
        document.getElementById('adv1').innerHTML ='';
        vp=1;
        }       }   
                    
        var winW = 600, winH = 400;
        if (document.body && document.body.offsetWidth) {
         winW = document.body.offsetWidth;
         winH = document.body.offsetHeight;
        }
        if (document.compatMode=='CSS1Compat' &&
            document.documentElement &&
            document.documentElement.offsetWidth ) {
         winW = document.documentElement.offsetWidth;
         winH = document.documentElement.offsetHeight;
        }
        if (window.innerWidth && window.innerHeight) {
         winW = window.innerWidth;
         winH = window.innerHeight;
        }

        var fkzd="177.206.184.253-36f6376e4d8bfedb4b4e28baf4393f43";

        var flashvars = {};
        flashvars.width=winW;
        flashvars.height=winH;
        flashvars.domain="http://www.nowvideo.sx";
        flashvars.file="hanu11wjzx2d7";
        flashvars.filekey=fkzd;
        flashvars.advURL="http://www.nowvideo.sx/video/hanu11wjzx2d7";

        var params = {};
        params.quality = "high";
        params.bgcolor = "#ffffff";
        params.allowscriptaccess = "sameDomain";
        params.allowfullscreen = "true";
        params.wmode = "transparent";
        var attributes = {};
        attributes.id = "videoPlayer";
        attributes.name = "videoPlayer";
        attributes.align = "middle";
        var xiSwfUrlStr = "";
        swfobject.embedSWF(
            "/player/nowvideo-v5.swf", "mediaspace", 
            winW, winH, 
            swfVersionStr, xiSwfUrlStr, 
            flashvars, params, attributes);
        <!-- JavaScript enabled so display the flashContent div in case it is not replaced with a swf object. -->
        swfobject.createCSS("#mediaspace", "display:block;text-align:left;");
        
        var e = document.getElementById("mediaspace");
        e.style.visibility = '';


    # 
    info for extracting
    # 
    When a page with a videonow video is request:
    + video now looks for uses the script above to find "key" and "file"
    + uses "key" and "file" to build a request to php script at "/api/player.api.php" with query params
    + params: {
        "cid3": "undefined", 
        "pass": "undefined", 
        "key": KEY_FROM_SCRIPT, 
        "user": "undefined", 
        "cid": "undefined", 
        "file": FILE_FROM_SCRIPT,
        "cid2": "undefined"
    }
    + this request return text with raw info for file in text

    example request: 
    --> http://www.nowvideo.sx/api/player.api.php?cid3=undefined&pass=undefined&key=177%2E206%2E184%2E253-36f6376e4d8bfedb4b4e28baf4393f43&user=undefined&numOfErrors=0&cid=undefined&file=hanu11wjzx2d7&cid2=undefined
    <-- url=http://s61.nowvideo.sx/dl/6e397df1b8128811dd4b2510f75db1f9/52660bfb/ff43ca5c13c8fbceae5af4f2a863a5f8e0.flv&title=Title%26asdasdas&site_url=http://www.nowvideo.sx/video/hanu11wjzx2d7&seekparm=&enablelimit=0

    where url=http://s61.nowvideo.sx/dl/6e397df1b8128811dd4b2510f75db1f9/52660bfb/ff43ca5c13c8fbceae5af4f2a863a5f8e0.flv
    is the raw url
    """

    def __init__(self):
        # super().__init__(self)
        super(NowVideoExtractor, self).__init__()
        self.host_list = ["nowvideo.eu", "nowvideo.ch"]
        self.holder_url = "http://embed.nowvideo.sx/embed.php?v={}"
        self.regex_url = None

    def raw_url(self, video_id):
        dest_url = self.holder_url.format(video_id)
        html_embed = str(urlopen(dest_url).read())

        # find "key" query param
        qparam_key = re.search(r'fkzd=["|\'](?P<key>[\w\s\.\-]+)["|\']', html_embed).group('key')

        # find "file" query param
        qparam_file = re.search(
            r'flashvars.file[\s=]+["|\'](?P<file>[\w]+)', html_embed).group('file')

        qparams = {
            "key": qparam_key,
            "file": qparam_file,
            "cid": "undefined",
            "cid2": "undefined",
            "cid3": "undefined",
            "user": "undefined",
            "pass": "undefined",
        }

        # build api request url with params to api
        api_url = "http://www.nowvideo.sx/api/player.api.php?{}".format(urlencode(qparams))

        # fetch response with containing raw url
        html_response = str(self.fetch_page(api_url))

        try:
            rgx = re.compile(r'url=(?P<rurl>http://[\w\.\-/&=?]+\.flv|mp4|avi|mk4|m4a)')
            url_found = re.search(rgx, html_response).group('rurl')
        except (IndexError, AttributeError):
            loggin.error('url was not found in response: {}'.format(html_response))

        return url_found


class GorillaVidExtractor(BaseExtractor):

    def __init__(self):
        # super().__init__(self)
        super(GorillaVidExtractor, self).__init__()
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
        # super().__init__(self)
        super(VidbullExtractor, self).__init__()
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
        pq = PyQuery(html_embed)
        script_text_raw = pq('#player_code script:not([src])').text()
        script_text = re.sub(r'\\', '', str(script_text_raw))

        rgx = re.compile(r"}\('(.+)',(\d+),(\d+),'([\w|]+)'")

        try:
            parg1 = re.search(rgx, script_text).group(1)
            parg2 = int(re.search(rgx, script_text).group(2))
            parg3 = int(re.search(rgx, script_text).group(3))
            parg4 = re.search(rgx, script_text).group(4).split('|')
        except:
            logging.error('ERROR trying to parse script text')
            return None
        try:
            unpacked_vars = self.unpacker(parg1, parg2, parg3, parg4)
        except:
            logging.error('ERROR trying unpack script text')
            return None
        try:
            raw = re.search(r'file:"([\w\.:/\-_]+)"', unpacked_vars).group(1)
        except:
            logging.error('ERROR file raw url not found in script unpacked')
            return None

        return raw

    def is_valid_url(self):
        pass


class DivxStageExtractor(BaseExtractor):

    """
    http://www.divxstage.eu/ to videonow

    example url: http://embed.divxstage.eu/embed.php?v=http://www.divxstage.eu/file/b04c4b011a81e&height=438&width=653

    find "key" and "file" query parameters
    example where found: <param name="flashvars" value="width=1920&amp;height=507&amp;domain=http://www.divxstage.eu&amp;file=httpwwwdivxstageeufileb04c4b011a81e&amp;filekey=177.206.184.253-94dc94e31c032d37fc9c1c6b12e7ae51&amp;advURL=http://www.divxstage.eu/video/httpwwwdivxstageeufileb04c4b011a81e">

    build api url from
    http://www.divxstage.eu/api/player.api.php?
    example: http://www.divxstage.eu/api/player.api.php?key=177%2E206%2E184%2E253-94dc94e31c032d37fc9c1c6b12e7ae51&file=httpwwwdivxstageeufileb04c4b011a81e
    
    return is a string with where url to video can be found
    example: url=http://t40.divxstage.eu/dl/cdf205451564ca45e342fbba2bf15b80/52662d51/ff58324d2c9602ce199e769dfa2b3296fc.flv&title=revenge.302.hdtvlolwso%26asdasdas&site_url=http://www.divxstage.eu/video/270b511691068&seekparm=&enablelimit=0
    """

    def __init__(self):
        # super().__init__(self)
        super(DivxStageExtractor, self).__init__()
        self.host_list = ["divxstage.eu"]
        self.holder_url = "http://embed.divxstage.eu/embed.php?&width=653&height=438&v={}"
        self.regex_url = None

    def raw_url(self, video_id):
        dest_url = self.holder_url.format(video_id)
        html_embed = self.fetch_page(dest_url)

        pq = PyQuery(html_embed)
        scripts_text = pq('body script').text()

        rgx = WiseUnpacker.param_regex

        # unpack script
        unpacked_script = None
        if re.search(rgx, scripts_text):
            # find unpack function params

            w = re.search(rgx, scripts_text).group('param_w')
            i = re.search(rgx, scripts_text).group('param_i')
            s = re.search(rgx, scripts_text).group('param_s')
            e = re.search(rgx, scripts_text).group('param_e')

            unpacked_script = WiseUnpacker.unpack(w, i, s, e)

        # find "key" param
        key_var_rgx = re.search(r'filekey=(\w+)', unpacked_script).group(1)
        key_param = re.search(key_var_rgx + r'="([\w\.\-]+)"', unpacked_script).group(1)
        # key_param = re.search(r'll="([\w\.\-]+)', unpacked_script).group(1)

        # find "file" param
        file_param = re.search(
            r'advURL="http://www\.divxstage\.eu/video/(\w+)"', unpacked_script).group(1)

        qparams = {
            "key": key_param,
            "file": file_param,
        }

        # call api to get result string containing raw url
        api_call = "http://www.divxstage.eu/api/player.api.php?" + urlencode(qparams)
        api_result = str(self.fetch_page(api_call))

        # extract raw url from api_call result
        url_found = None
        try:
            rgx = re.compile(r'url=(?P<rurl>http://[\w\.\-/=]+\.flv|mp4|avi|mk4|m4a)')
            url_found = rgx.search(api_result).group('rurl')
        except (IndexError, AttributeError):
            return None

        return(url_found)

EXTRACTOR_INSTANCES = (
    GorillaVidExtractor(),
    VidbullExtractor(),
    NowVideoExtractor(),
    DivxStageExtractor(),
)


def get_extractors():
    return EXTRACTOR_INSTANCES


def get_by_url(url):
    for extractor in get_extractors():
        if extractor.is_valid_url(url):
            return extractor


def get_by_hostname(hostname):
    for extractor in get_extractors():
        if extractor.is_valid_host(hostname):
            return extractor

if __name__ == '__main__':
    extor = DivxStageExtractor()
    extor.raw_url('b04c4b011a81e')
