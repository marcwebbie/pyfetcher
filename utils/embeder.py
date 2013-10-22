
class GorillaVidExtractor:
    host_list = ["gorillavid", "gorillavid.in"]
    holder_url = "http://gorillavid.in/embed-{}-650x400.html"

    @staticmethod
    def is_valid_url(self, url):
        pass

    @staticmethod
    def is_valid_host(host):
        return host in self.host_list

    @staticmethod
    def raw_url(url):
        pass


hosts = {
    "vidbux.com": "http://www.vidbux.com/embed-{}-width-653-height-400.html",
    "vidbull.com": "http://vidbull.com/embed-{}-650x328.html",
    "gorillavid.com": "http://gorillavid.in/embed-{}-650x400.html",
    "gorillavid.in": "http://gorillavid.in/embed-{}-650x400.html",
    "vidxden.com": "http://www.vidxden.com/embed-{}.html",
    "divxden.com": "http://www.vidxden.com/embed-{}.html",
    "novamov.com": "http://embed.novamov.com/embed.php?width=653&height=525&px=1&v={}",
    'mooshare.biz': "http://mooshare.biz/embed-{}-650x400.html",
    '180upload.com': "http://180upload.com/embed-{}-650x370.html",
    "videoweed.es": 'http://embed.videoweed.es/embed.php?v={}&width="653"&height="525"',
    "videoweed.com": 'http://embed.videoweed.es/embed.php?v={}&width=653&height=525',
    "movshare.net": 'http://www.movshare.net/embed/{}/?width=655&height=362',
    "nowvideo.eu": 'http://embed.nowvideo.eu/embed.php?v={}&width=650&height=510'
}


"""
javascript:show('bvh6tj8vlwsc','The%20Vampire%20Diaries%20Season%203%20Episode%2017',%20'vidbull.com');
<param name="flashvars" value="width=1920&amp;height=484&amp;domain=http://www.videoweed.es&amp;file=11f07e87a450d&amp;filekey=177.206.191.64-1fb13a749292c37c12161fc1eca7b355-&amp;advURL=http://www.videoweed.es/file/11f07e87a450d">
javascript:show('11f07e87a450d','The Vampire Diaries Season 1 Episode 1', 'videoweed.es');
javascript:show('6ymnjwqddcc0b','The Vampire Diaries Season 1 Episode 1', 'movshare.net');
javascript:show('v4cnayam8932r','The Vampire Diaries Season 1 Episode 1', 'nowvideo.eu');
<param name="flashvars" value="width=960&amp;height=500&amp;domain=http://www.nowvideo.sx&amp;file=v4cnayam8932r&amp;filekey=177.206.191.64-2c820acbfc8b8504e2e2446b667ed693&amp;advURL=0&amp;autoplay=false&amp;cid=1&amp;premiumLink=http://www.nowvideo.sx/premium.php">
"""
