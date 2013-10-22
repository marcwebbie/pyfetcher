if(vhost == "youtube"){
        document.getElementById("vvdiv").innerHTML = emb_title + emb_div_open + '\
                                                                                                <object width="640" height="505">\
                                                                                                        <param value="http://www.youtube.com/v/' + vid + '&hl=en_US&fs=1&rel=0&color1=0x65786C&color2=0x7E9687&hd=1" name="movie"/>\
                                                                                                        <param value="true" name="allowFullScreen"/>\
                                                                                                        <param value="always" name="allowscriptaccess"/>\
                                                                                                        <embed width="640" height="505" allowfullscreen="true" allowscriptaccess="always" type="application/x-shockwave-flash" src="http://www.youtube.com/v/' + vid + '&hl=en_US&fs=1&rel=0&color1=0x7E9687&color2=0x65786C&hd=1"/>\
                                                                                                    </object>' + emb_div_close + eml_html;
    }
    else if(vhost == "sta" + "gevu.com"){
        iframewidth = 655;
        iframeheight = 535;
        hide_px = 28;
        document.getElementById("vvdiv").innerHTML = emb_title + emb_div_open + "\
                                                                                                    <div style='position:relative; height:" + (iframeheight - hide_px) + "px; width:" + iframewidth + "px;'>\
                                                                                                        <div style='clip:rect(" + hide_px + "px " + iframewidth + "px " + iframeheight + "px 0px); position:absolute; top:-" + hide_px + "px; left:0px;'>\
                                                                                                        <iframe style='overflow: hidden; border: 0; width: " + iframewidth + "px; height: " + iframeheight + "px' src='http://sta" + "gevu.com/embed?width=" + iframewidth + "&height=" + (iframeheight - 35) + "&background=000&uid=" + vid + "' scrolling='no'></iframe>\
                                                                                                    </div>\
                                                                                                    </div>" + emb_div_close + eml_html;
    }
    else if(vhost == "mov" + "share.net"){
        iframewidth = 655;
        iframeheight = 362;
        hide_px = 26;
        nav_px = 36;
        document.getElementById("vvdiv").innerHTML = emb_title + emb_div_open + "\
                                                                                                    <div style='position:relative; height:" + (iframeheight + nav_px - hide_px) + "px; width:" + iframewidth + "px;'>\
                                                                                                        <div style='clip:rect(" + hide_px + "px " + iframewidth + "px " + (iframeheight + nav_px) + "px 0px); position:absolute; top:-" + hide_px + "px; left:0px;'>\
                                                                                                        <iframe style='overflow: hidden; border: 0; width: " + iframewidth + "px; height: " + (iframeheight + nav_px) + "px' src='http://www.mov" + "share.net/embed/" + vid + "/?width=" + iframewidth + "&height=" + iframeheight + "' scrolling='no'></iframe>\
                                                                                                    </div>\
                                                                                                    </div>" + emb_div_close + eml_html;
    }
    else if(vhost == "vid" + "bux.com"){
        iframewidth = 653;
        iframeheight = 400;
        hide_px = 30;
        nav_px = 0;
        document.getElementById("vvdiv").innerHTML = emb_title + emb_div_open + "\
                                                                                                    <div style='position:relative; height:" + (iframeheight + nav_px - hide_px) + "px; width:" + iframewidth + "px;'>\
                                                                                                        <div style='clip:rect(" + hide_px + "px " + iframewidth + "px " + (iframeheight + nav_px) + "px 0px); position:absolute; top:-" + hide_px + "px; left:0px;'>\
                                                                                                        <iframe style='overflow: hidden; border: 0; width: " + iframewidth + "px; height: " + (iframeheight + nav_px) + "px' src='http://www.vid" + "bux.com/embed-" + vid + "-width-" + iframewidth + "-height-" + iframeheight + ".html' scrolling='no'></iframe>\
                                                                                                    </div>\
                                                                                                    </div>" + emb_div_close + eml_html;
    }
    else if(vhost == "video" + "weed.com" || vhost == "video" + "weed.es"){
        iframewidth = 653;
        iframeheight = 525;
        hide_px = 45;
        nav_px = 0;
        document.getElementById("vvdiv").innerHTML = emb_title + emb_div_open + "\
                                                                                                    <div style='position:relative; height:" + (iframeheight + nav_px - hide_px) + "px; width:" + iframewidth + "px;'>\
                                                                                                        <div style='clip:rect(" + hide_px + "px " + iframewidth + "px " + (iframeheight + nav_px) + "px 0px); position:absolute; top:-" + hide_px + "px; left:0px;'>\
                                                                                                        <iframe style='overflow: hidden; border: 0; width: " + iframewidth + "px; height: " + (iframeheight + nav_px) + "px' src='http://embed.video" + "weed.es/embed.php?v=" + vid + "&width=" + iframewidth + "&height=" + iframeheight + "' scrolling='no'></iframe>\
                                                                                                    </div>\
                                                                                                    </div>" + emb_div_close + eml_html;
    }
    else if(vhost == "put" + "locker.com"){
        iframewidth = 653;
        iframeheight = 394;
        hide_px = 25;
        nav_px = 0;
        document.getElementById("vvdiv").innerHTML = emb_title + emb_div_open + "\
                                                                                                    <div style='position:relative; height:" + (iframeheight + nav_px - hide_px) + "px; width:" + iframewidth + "px;'>\
                                                                                                        <div style='clip:rect(" + hide_px + "px " + iframewidth + "px " + (iframeheight + nav_px) + "px 0px); position:absolute; top:-" + hide_px + "px; left:0px;'>\
                                                                                                        <iframe style='overflow: hidden; border: 0; width: " + iframewidth + "px; height: " + (iframeheight + nav_px) + "px' src='http://www.put" + "locker.com/embed/" + vid + "' width='" + iframewidth + "' scrolling='no'></iframe>\
                                                                                                    </div>\
                                                                                                    </div>" + emb_div_close + eml_html;
    }
    else if(vhost == "sock" + "share.com"){
        iframewidth = 653;
        iframeheight = 394;
        hide_px = 25;
        nav_px = 0;
        document.getElementById("vvdiv").innerHTML = emb_title + emb_div_open + "\
                                                                                                    <div style='position:relative; height:" + (iframeheight + nav_px - hide_px) + "px; width:" + iframewidth + "px;'>\
                                                                                                        <div style='clip:rect(" + hide_px + "px " + iframewidth + "px " + (iframeheight + nav_px) + "px 0px); position:absolute; top:-" + hide_px + "px; left:0px;'>\
                                                                                                        <iframe style='overflow: hidden; border: 0; width: " + iframewidth + "px; height: " + (iframeheight + nav_px) + "px' src='http://www.sock" + "share.com/embed/" + vid + "' width='" + iframewidth + "' scrolling='no'></iframe>\
                                                                                                    </div>\
                                                                                                    </div>" + emb_div_close + eml_html;
    }
    else if(vhost == "video" + "bb.com"){
        iframewidth = 653;
        iframeheight = 558;
        hide_px = 90;
        nav_px = 0;
        document.getElementById("vvdiv").innerHTML = emb_title + emb_div_open + "\
                                                                                                    <div style='position:relative; height:" + (iframeheight + nav_px - hide_px) + "px; width:" + iframewidth + "px;'>\
                                                                                                        <div style='clip:rect(" + hide_px + "px " + iframewidth + "px " + (iframeheight + nav_px) + "px 0px); position:absolute; top:-" + hide_px + "px; left:0px;'>\
                                                                                                        <object id='player' width='" + iframewidth + "' height='" + iframeheight + "' classid='clsid:d27cdb6e-ae6d-11cf-96b8-444553540000' >\
                                                                                                            <param name='movie' value='http://video" + "bb.com/e/" + vid + "' ></param>\
                                                                                                            <param name='allowFullScreen' value='true' ></param>\
                                                                                                            <param name='allowscriptaccess' value='always'></param>\
                                                                                                            <param name='wmode' value='transparent' />\
                                                                                                            <embed src='http://vide" + "obb.com/e/" + vid + "' type='application/x-shockwave-flash' allowscriptaccess='always' allowfullscreen='true' wmode='transparent' width='" + iframewidth + "' height='" + iframeheight + "'></embed>\
                                                                                                        </object>\
                                                                                                    </div>\
                                                                                                    </div>" + emb_div_close + eml_html;
    }
    else if(vhost == "divx" + "den.com" || vhost == "vidx" + "den.com"){
        iframewidth = 653;
        iframeheight = 362;
        hide_px = 30;

        document.getElementById("vvdiv").innerHTML = emb_title + emb_div_open + "\
                                                                                                    <div style='position:relative; height:" + (iframeheight - hide_px) + "px; width:" + iframewidth + "px;'>\
                                                                                                        <div style='clip:rect(" + hide_px + "px " + iframewidth + "px " + iframeheight + "px 0px); position:absolute; top:-" + hide_px + "px; left:0px;'>\
                                                                                                            <iframe scrolling='no' src='http://www.vidx" + "den.com/embed-" + vid + ".html' width='" + iframewidth + "' height='" + iframeheight + "' frameborder='0' border='0'></iframe>\
                                                                                                        </div>\
                                                                                                    </div>" + emb_div_close + eml_html;                 
    }
    else if(vhost == "tudou"){
        document.getElementById("vvdiv").innerHTML = emb_title + emb_div_open + "\
                                                                                                    <object\
                                                                                                     type='application/x-shockwave-flash'\
                                                                                                     data='http://www.tu" + "dou.com/v/" + vid + "/v.swf'\
                                                                                                     width='650'\
                                                                                                     height='500'>\
                                                                                                     <param name='movie' value='http://www.tu" + "dou.com/v/" + vid + "/v.swf'>\
                                                                                                    </object>" + emb_div_close + eml_html;
    }
    else if(vhost == "nova" + "mov.com"){
        document.getElementById("vvdiv").innerHTML = emb_title + emb_div_open + '\
                                                                                                <iframe framespacing="0" scrolling="no" frameborder="0" width="653" height="525" src="http://embed.nova' + 'mov.com/embed.php?width=653&height=525&px=1&v=' + vid + '"></iframe>' + emb_div_close + eml_html;                   
    }
    else if(vhost == "divx" + "stage.eu"){
        document.getElementById("vvdiv").innerHTML = emb_title + emb_div_open + '\
                                                                                                <iframe framespacing="0" scrolling="no" frameborder="0" width="653" height="460" src="http://embed.divx' + 'stage.eu/embed.php?&width=653&height=438&v=' + vid + '"></iframe>' + emb_div_close + eml_html;                  
    }
    else if(vhost == "you" + "ku"){
        document.getElementById("vvdiv").innerHTML = emb_title + emb_div_open + '\
                                                                                                <embed src="http://player.you' + 'ku.com/player.php/sid/' + vid + '=/v.swf" quality="high" width="480" height="400" align="middle" allowScriptAccess="sameDomain" type="application/x-shockwave-flash"></embed>' + emb_div_close + eml_html;
    }
    else if(vhost == "smo" + "tri.com"){
        document.getElementById("vvdiv").innerHTML = emb_title + emb_div_open + '\
                                                                                                <object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" width="640" height="360"><param name="movie" value="http://pics.smo' + 'tri.com/scrubber_custom8.swf?file=' + vid + '&bufferTime=3&autoStart=false&str_lang=rus&xmlsource=http%3A%2F%2Fpics%2Esmotri%2Ecom%2Fcskins%2Fblue%2Fskin%5Fcolor%2Exml&xmldatasource=http%3A%2F%2Fpics%2Esmotri%2Ecom%2Fcskins%2Fblue%2Fskin%5Fng%2Exml" /><param name="allowScriptAccess" value="always" /><param name="allowFullScreen" value="true" /><param name="bgcolor" value="#7E9687" /><embed src="http://pics.smo' + 'tri.com/scrubber_custom8.swf?file=' + vid + '&bufferTime=3&autoStart=false&str_lang=rus&xmlsource=http%3A%2F%2Fpics%2Esmotri%2Ecom%2Fcskins%2Fblue%2Fskin%5Fcolor%2Exml&xmldatasource=http%3A%2F%2Fpics%2Esmotri%2Ecom%2Fcskins%2Fblue%2Fskin%5Fng%2Exml" quality="high" allowscriptaccess="always" allowfullscreen="true" wmode="window"  width="640" height="360" type="application/x-shockwave-flash"></embed></object><br /><strong><a href="http://smo' + 'tri.com/video/view/?id=' + vid + '" target="_blank"></strong>' + emb_div_close + eml_html;
    }
    else if(vhost == "video" + "zer.com"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <object id="player" width="653" height="460" classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" >\
                                                                                                        <param name="movie" value="http://www.video' + 'zer.com/embed/<?php print $id; ?>" ></param>\
                                                                                                        <param name="allowFullScreen" value="true" ></param>\
                                                                                                        <embed src="http://www.video' + 'zer.com/embed/' + vid + '" type="application/x-shockwave-flash" allowfullscreen="true" width="653" height="460">\
                                                                                                        </embed>\
                                                                                                    </object>' + emb_div_close + eml_html;
    }
    else if(vhost == "vee" + "vr.com"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <iframe src="http://vee' + 'vr.com/embed/' + vid + '?w=653&h=370" width="653" height="370" scrolling="no" frameborder="0">' + emb_div_close + eml_html;
    }
    else if(vhost == "ov" + "file.com"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <IFRAME SRC="http://ov' + 'file.com/embed-' + vid + '-650x325.html" FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO WIDTH=650 HEIGHT=340></IFRAME>' + emb_div_close + eml_html;
    }
    else if(vhost == "gorilla" + "vid.com" || vhost == "gorilla" + "vid.in"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <IFRAME SRC="http://gorillavid.in/embed-' + vid + '-650x400.html" FRAMEBORDER="0" MARGINWIDTH="0" MARGINHEIGHT="0" SCROLLING="NO" WIDTH="650" HEIGHT="400"></IFRAME>' + emb_div_close + eml_html;
        
        //document.getElementById("vvdiv").innerHTML =  emb_title + emb_div_open + '\
        //                                                                                          <object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" width="650" height="400">\
        //                                                                                              <param name="movie" value="http://gorilla' + 'vid.in/player/player.swf">\
        //                                                                                              <param name="allowfullscreen" value="true">\
        //                                                                                              <param name="wmode" value="opaque">\
        //                                                                                              <param name="flashvars" value="file=http://gorilla' + 'vid.in/vidembed-' + vid + '.avi&provider=http">\
        //                                                                                              <embed src="http://gorilla' + 'vid.in/player/player.swf" width="650" height="400" bgcolor="#000000" allowfullscreen="true" flashvars="file=http://gorilla' + 'vid.in/vidembed-' + vid + '.avi&provider=http" />\
        //                                                                                          </object>' + emb_div_close + eml_html;
    }
    else if(vhost == "za" + "laa.com"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <IFRAME SRC="http://www.za' + 'laa.com/embed-' + vid + '.html" FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO WIDTH=650 HEIGHT=393></IFRAME>' + emb_div_close + eml_html;
    }
    else if(vhost == "file" + "box.com"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <IFRAME SRC="http://www.file' + 'box.com/embed-' + vid + '-650x450.html" FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO WIDTH=650 HEIGHT=450></IFRAME>' + emb_div_close + eml_html;
    }
    else if(vhost == "much" + "share.net"){
        total_width = 660;
        total_height = 413;
        hide_px = 50;
        hide_left_px = 0;
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <div style="position:relative; height:' + (total_height - hide_px) + 'px; width:' + (total_width - hide_left_px) + 'px;">\
                                                                                                        <div style="clip:rect(' + hide_px + 'px ' + total_width + 'px ' + total_height + 'px ' + hide_left_px + 'px); position:absolute; top:-' + hide_px + 'px; left:-' + hide_left_px + 'px;">\
                                                                                                        <iframe WIDTH=660 HEIGHT=413 frameborder="0" src="http://much' + 'share.net/embed-' + vid + '.html" scrolling="no"></iframe>\
                                                                                                        </div>\
                                                                                                    </div>\
                                                                                                    ' + emb_div_close + eml_html;
    }
    else if(vhost == "upload" + "c.com"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <IFRAME SRC="http://www.upload' + 'c.com/embed-' + vid + '.html" FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO WIDTH=650 HEIGHT=369></IFRAME>' + emb_div_close + eml_html;
    }
    else if(vhost == "movie" + "zer.com"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <iframe width="650" height="400" src="http://movie' + 'zer.com/e/' + vid + '" frameborder="0" scrolling="no" allowfullscreen></iframe>' + emb_div_close + eml_html;
    }
    else if(vhost == "stream" + "2k.com"){
        lparts = vid.split(".");
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=9,0,0,0" width="650" height="400">\
                                                                                                        <param name="allowFullScreen" value="true">\
                                                                                                        <param name="movie" value="' + lparts[0] + '.stream' + '2k.com/playerjw/player-licensed56.swf">\
                                                                                                        <param name="quality" value="high">\
                                                                                                        <param name="bgcolor" value="#000000">\
                                                                                                        <param name="wmode" value="transparent"> \
                                                                                                        <param name="flashvars" value="config=' + vid + '">\
                                                                                                        <embed wmode="transparent" type="application/x-shockwave-flash" pluginspage="http://www.macromedia.com/go/getflashplayer"  src="' + lparts[0] + '.stream' + '2k.com/playerjw/player-licensed56.swf" width="650" height="400" allowscriptaccess="always" allowfullscreen="true" flashvars="config=' + vid + '" />\
                                                                                                    </object>' + emb_div_close + eml_html;
    }
    else if(vhost == "vid" + "hog.com"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <IFRAME SRC="http://www.vid' + 'hog.com/embed-' + vid + '.html" FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO WIDTH=600 HEIGHT=320></IFRAME>' + emb_div_close + eml_html;
    }
    else if(vhost == "hosting" + "bulk.com"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <iframe src="http://hosting' + 'bulk.com/embed-' + vid + '-650x350.html" frameborder="0" marginheight="0" marginheight="0" scrolling="no" width="650" height="350"></iframe>' + emb_div_close + eml_html;
    }
    else if(vhost == "u" + "fliq.com"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <IFRAME SRC="http://www.u' + 'fliq.com/embed-' + vid + '-650x400.html" FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO WIDTH=650 HEIGHT=400></IFRAME>' + emb_div_close + eml_html;
    }
    else if(vhost == "xvid" + "stage.com"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <IFRAME SRC="http://xvid' + 'stage.com/embed-' + vid + '.html" FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO WIDTH=640 HEIGHT=360></IFRAME>' + emb_div_close + eml_html;
    }
    else if(vhost == "video" + "pp.com"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <iframe src="http://video' + 'pp.com/player.php?code=' + vid + '" width="640" height="360" scrolling="no" frameborder="0"></iframe>' + emb_div_close + eml_html;
    }
    else if(vhost == "now" + "video.eu" || vhost == "now" + "video.ch"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <iframe width="650" height="510" frameborder="0" src="http://embed.now' + 'video.eu/embed.php?v=' + vid + '&width=650&height=510" scrolling="no"></iframe>' + emb_div_close + eml_html;
    }
    else if(vhost == "watch" + "freeinhd.com"){
        total_width = 725;
        total_height = 600;
        hide_px = 40;
        hide_left_px = 0;
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <div style="position:relative; height:' + (total_height - hide_px) + 'px; width:' + (total_width - hide_left_px) + 'px;">\
                                                                                                        <div style="clip:rect(' + hide_px + 'px ' + total_width + 'px ' + total_height + 'px ' + hide_left_px + 'px); position:absolute; top:-' + hide_px + 'px; left:-' + hide_left_px + 'px;">\
                                                                                                        <iframe src="http://www.watch' + 'freeinhd.com/embed/' + vid + '" width="725" height="600" scrolling="no" frameborder="0"></iframe>\
                                                                                                        </div>\
                                                                                                    </div>\
                                                                                                    ' + emb_div_close + eml_html;
    }
    else if(vhost == "flash" + "x.tv"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <iframe width="600" height="370" src="http://play.flash' + 'x.tv/player/embed.php?hash=' + vid + '&width=650&height=410&autoplay=no" frameborder="0" allowfullscreen></iframe>' + emb_div_close + eml_html;
    }
    else if(vhost == "v" + "reer.com"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <IFRAME SRC="http://v' + 'reer.com/embed-' + vid + '-650x400.html" FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO WIDTH=650 HEIGHT=400></IFRAME>' + emb_div_close + eml_html;
    }
    else if(vhost == "nos" + "video.com"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <IFRAME SRC="http://nos' + 'video.com/embed/' + vid + '/650x370" FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO WIDTH=650 HEIGHT=390></IFRAME>' + emb_div_close + eml_html;
    }
    else if(vhost == "divx" + "base.com"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <IFRAME SRC="http://www.divx' + 'base.com/embed-' + vid + '-650x440.html" FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO WIDTH=650 HEIGHT=460></IFRAME>' + emb_div_close + eml_html;
    }
    else if(vhost == "da" + "clips.in"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <IFRAME SRC="http://da' + 'clips.in/embed-' + vid + '-650x350.html" FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO WIDTH=650 HEIGHT=500></IFRAME>' + emb_div_close + eml_html;
    }
    else if(vhost == "mov" + "pod.in"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <IFRAME SRC="http://mov' + 'pod.in/embed-' + vid + '-650x350.html" FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO WIDTH=650 HEIGHT=500></IFRAME>' + emb_div_close + eml_html;
    }
    else if(vhost == "mov" + "reel.com"){
        total_width = 607;
        total_height = 470;
        hide_px = 62;
        hide_left_px = 0;
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <div style="position:relative; height:' + (total_height - hide_px) + 'px; width:' + (total_width - hide_left_px) + 'px;">\
                                                                                                        <div style="clip:rect(' + hide_px + 'px ' + total_width + 'px ' + total_height + 'px ' + hide_left_px + 'px); position:absolute; top:-' + hide_px + 'px; left:-' + hide_left_px + 'px;">\
                                                                                                            <iframe src="http://mov' + 'reel.com/embed/' + vid + '" width=607 height=470 border=0 frameborder=0 scrolling=no></iframe>\
                                                                                                        </div>\
                                                                                                    </div>' + emb_div_close + eml_html;
    }
    else if(vhost == "180" + "upload.com"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <IFRAME SRC="http://180' + 'upload.com/embed-' + vid + '-650x370.html" FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO WIDTH=650 HEIGHT=390></IFRAME>' + emb_div_close + eml_html;
    }
    else if(vhost == "moo" + "share.biz"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <IFRAME SRC="http://moo' + 'share.biz/embed-' + vid + '-650x400.html" FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO WIDTH=650 HEIGHT=420></IFRAME>' + emb_div_close + eml_html;
    }
    else if(vhost == "vid" + "bull.com"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <IFRAME SRC="http://vid' + 'bull.com/embed-' + vid + '-650x328.html" FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO WIDTH=650 HEIGHT=348></IFRAME>' + emb_div_close + eml_html;
    }
    else if(vhost == "glumbo" + "uploads.com"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <IFRAME SRC="http://glumbo' + 'uploads.com/embed-' + vid + '-650x390.html" FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO WIDTH=650 HEIGHT=390></IFRAME>' + emb_div_close + eml_html;
    }
    else if(vhost == "modo" + "video.com"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <IFRAME SRC="http://www.modo' + 'video.com/frame.php?v=' + vid + '" FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO WIDTH=650 HEIGHT=400></IFRAME>' + emb_div_close + eml_html;
    }
    else if(vhost == "all" + "myvideos.net"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <IFRAME SRC="http://allmy' + 'videos.net/embed-' + vid + '-650x360.html" FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO WIDTH=650 HEIGHT=360></IFRAME>' + emb_div_close + eml_html;
    }
    else if(vhost == "vid" + "up.me"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <IFRAME SRC="http://vid' + 'up.me/embed-' + vid + '-650x350.html" FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO WIDTH=650 HEIGHT=350></IFRAME>' + emb_div_close + eml_html;
    }
    else if(vhost == "video" + "bam.com"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <IFRAME SRC="http://video' + 'bam.com/widget/' + vid + '/custom/650" FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO WIDTH=650 HEIGHT=415></IFRAME>' + emb_div_close + eml_html;
    }
    else if(vhost == "xvid" + "stream.net"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <IFRAME SRC="http://xvid' + 'stream.net/embed-' + vid + '.html" FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO WIDTH=720 HEIGHT=380></IFRAME>' + emb_div_close + eml_html;
    }
    else if(vhost == "ve" + "oh.com"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <object width="650" height="500" id="veohFlashPlayer" name="veohFlashPlayer">\
                                                                                                        <param name="movie" value="http://www.ve' + 'oh.com/swf/webplayer/WebPlayer.swf?version=AFrontend.5.7.0.1404&permalinkId=' + vid + '&player=videodetailsembedded&videoAutoPlay=0&id=anonymous"></param>\
                                                                                                        <param name="allowFullScreen" value="true"></param>\
                                                                                                        <param name="allowscriptaccess" value="always"></param>\
                                                                                                        <embed src="http://www.ve' + 'oh.com/swf/webplayer/WebPlayer.swf?version=AFrontend.5.7.0.1404&permalinkId=' + vid + '&player=videodetailsembedded&videoAutoPlay=0&id=anonymous" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="650" height="500" id="veohFlashPlayerEmbed" name="veohFlashPlayerEmbed"></embed>\
                                                                                                    </object>' + emb_div_close + eml_html;
    }
    else if(vhost == "fle" + "on.me"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <iframe src="http://fle' + 'on.me/videos.php?Id=' + vid + '" frameborder="0" height="518" width="750" scrolling="no"></iframe>' + emb_div_close + eml_html;
    }
    else if(vhost == "share" + "six.com"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <iframe src="http://yourproxy' + 'video.com/embed/share' + 'six.php?getvid=http://share' + 'six.com/' + vid + '" frameborder="0" height="470" width="580" scrolling="no"></iframe>' + emb_div_close + eml_html;
    }
    else if(vhost == "flash" + "x.tv"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <iframe src="http://play.flash' + 'x.tv/player/embed.php?hash=' + vid + '&width=650&height=500&autoplay=yes" frameborder="0" height="500" width="650" scrolling="no"></iframe>' + emb_div_close + eml_html;
    }
    else if(vhost == "video" + "slasher.com"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <iframe src="http://www.video' + 'slasher.com/embed/' + vid + '" width="650" height="400" frameborder="0" scrolling="no"></iframe>' + emb_div_close + eml_html;
    }
    else if(vhost == "billion" + "uploads.com"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <iframe src="http://billion' + 'uploads.com/embed-' + vid + '-650x330.html" width="650" height="463" frameborder="0" scrolling="no"></iframe>' + emb_div_close + eml_html;
    }
    else if(vhost == "i" + "shared.eu"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <iframe src="http://i' + 'shared.eu/embed/' + vid + '?width=650&height=360" width="650" height="360" frameborder="0" scrolling="no"></iframe>' + emb_div_close + eml_html;
    }
    else if(vhost == "mighty" + "upload.com"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <iframe src="http://www.mighty' + 'upload.com/embed-' + vid + '-650x357.html" width="650" height="357" frameborder="0" scrolling="no"></iframe>' + emb_div_close + eml_html;
    }
    else if(vhost == "vid" + "play.net"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <iframe src="http://vid' + 'play.net/embed-' + vid + '-650x367.html" width="650" height="367" frameborder="0" scrolling="no"></iframe>' + emb_div_close + eml_html;
    }
    else if(vhost == "video" + "mega.tv"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <iframe src="http://video' + 'mega.tv/iframe.php?ref=' + vid + '&width=650&height=340" width="650" height="340" frameborder="0" scrolling="no"></iframe>' + emb_div_close + eml_html;
    }
    else if(vhost == "royal" + "vids.eu"){
        document.getElementById("vvdiv").innerHTML =    emb_title + emb_div_open + '\
                                                                                                    <IFRAME SRC="http://royal' + 'vids.eu/embed-' + vid + '-650x430.html" FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO WIDTH=650 HEIGHT=430></IFRAME>' + emb_div_close + eml_html;
    }
    else if(("  " + vid).indexOf("http://") > 0){
        window.open(vid);
    }