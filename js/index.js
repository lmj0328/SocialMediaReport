first();

async function first() {
    if (document.location.search == "") {
        renderMainPage();
    } else {
        $('#backdrop').addClass('hidden');
        $('#user-input-form').addClass('hidden');
        $("#landing-page").addClass("hidden");
        $('html').removeClass('disable-scroll');
        $("#report-template").removeClass("hidden");

        // fetch twitter data
        // const twitter_res = await fetch(`data_insights/twitter_sample.json`);
        // const twitter_json = await twitter_res.json();

        // fetch facebook data
        // const facebook_res = await fetch(`data_insights/facebook_sample.json`);
        // const facebook_json = await facebook_res.json();

        // fetch instagram data
        // const instagram_res = await fetch(`data_insights/instagram_sample.json`);
        // const instagram_json = await instagram_res.json();

        const res = await fetch(`data_insights/sample.json`);
        const json = await res.json();
        console.log(json);

        var data = getQueryParams(document.location.search)

        renderReport(json, data);
        
    }
}



// render landing page
function renderMainPage() {
    $(window).scroll(function() {
        // when window scroll, switch navigation bar stylesheet
        if($(document).scrollTop() > 50) {
            $("#navigation-bar nav").addClass("scrolled");
            $("#navigation-bar .navbar-brand span").addClass("scrolled");
            $("#navigation-bar .navbar-nav li a").addClass("scrolled");
            $("#navigation-bar .navbar-nav i").addClass("scrolled");    
        } else {
            $("#navigation-bar nav").removeClass("scrolled");
            $("#navigation-bar .navbar-brand span").removeClass("scrolled");
            $("#navigation-bar .navbar-nav li a").removeClass("scrolled");
            $("#navigation-bar .navbar-nav i").removeClass("scrolled");    
        } 

        var scroll = window.requestAnimationFrame || function(callback) {
            window.setTimeout(callback,1000/60)
        };

        let revealOnScroll = document.querySelectorAll('.revealOnScroll');
        function checkifInView() {
            revealOnScroll.forEach((element) => {
                if(isElementInViewport(element)) {
                    $(element).addClass('current');
                    $(element).addClass('revealed');
                } else {
                    $(element).removeClass('current');
                    // $(element).removeClass('revealed');

                }
            })
            
        }

        checkifInView();
    });

    // $('#explore-project').click(function() {
    //     $('#backdrop').removeClass('hidden');
    //     $('#user-input-form').removeClass('hidden');
    //     $('html').addClass('disable-scroll');
    // });

    $('#banner-cross').click(function() {
        $('#banner').addClass('hidden');
    });


    $('#cross-btn').click(function() {
        $('#backdrop').addClass('hidden');
        $('#user-input-form').addClass('hidden');
        $('html').removeClass('disable-scroll');
    });

    // $('#get-report').click(function() {
    //     $.ajax({
    //         dataType: "json",
    //         url: "data_insights/sample.json",
    //         jsonp: "$callback",
    //         success: renderReport
    //     })
    //   renderReport(json, )
    // });
}





function renderReport(json, user_data) {

    console.log(json);
    console.log(user_data);


    $("#report-tmpl").tmpl(user_data).appendTo("#report-template");

    !function(a){
        "function"==typeof define&&define.amd?define(["jquery"],a):"object"==typeof exports?module.exports=a:a(jQuery)
    }(function(a){
        function b(b){
            var g=b||window.event,h=i.call(arguments,1),j=0,l=0,m=0,n=0,o=0,p=0;
            if(b=a.event.fix(g),
                b.type="mousewheel",
                "detail"in g&&(m=-1*g.detail),
                "wheelDelta"in g&&(m=g.wheelDelta),
                "wheelDeltaY"in g&&(m=g.wheelDeltaY),
                "wheelDeltaX"in g&&(l=-1*g.wheelDeltaX),
                "axis"in g&&g.axis===g.HORIZONTAL_AXIS&&(l=-1*m,m=0),j=0===m?l:m,"deltaY"in g&&(m=-1*g.deltaY,j=m),
                "deltaX"in g&&(l=g.deltaX,0===m&&(j=-1*l)),0!==m||0!==l)
                {
                    if(1===g.deltaMode){
                        var q=a.data(this,"mousewheel-line-height");
                        j*=q,m*=q,l*=q
                    }else if(2===g.deltaMode){
                        var r=a.data(this,"mousewheel-page-height");
                        j*=r,m*=r,l*=r
                    }
                    if(n=Math.max(Math.abs(m),Math.abs(l)),
                        (!f||f>n)&&(f=n,d(g,n)&&(f/=40)),
                        d(g,n)&&(j/=40,l/=40,m/=40),
                        j=Math[j>=1?"floor":"ceil"](j/f),
                        l=Math[l>=1?"floor":"ceil"](l/f),
                        m=Math[m>=1?"floor":"ceil"](m/f),
                        k.settings.normalizeOffset&&this.getBoundingClientRect) {
                            var s=this.getBoundingClientRect();
                            o=b.clientX-s.left,p=b.clientY-s.top
                    }
                    return b.deltaX=l,
                        b.deltaY=m,
                        b.deltaFactor=f,
                        b.offsetX=o,
                        b.offsetY=p,
                        b.deltaMode=0,
                        h.unshift(b,j,l,m),
                        e&&clearTimeout(e),
                        e=setTimeout(c,200),
                        (a.event.dispatch||a.event.handle).apply(this,h)
            }
        }
    
        function c(){
            f=null
        }
    
        function d(a,b){
            return k.settings.adjustOldDeltas&&"mousewheel"===a.type&&b%120===0
        }
    
        var e,f,g=["wheel","mousewheel","DOMMouseScroll","MozMousePixelScroll"],h="onwheel"in document||document.documentMode>=9?["wheel"]:["mousewheel","DomMouseScroll","MozMousePixelScroll"],i=Array.prototype.slice;
        
        if(a.event.fixHooks) {
            for(var j=g.length;j;)a.event.fixHooks[g[--j]]=a.event.mouseHooks;
        }
        var k=a.event.special.mousewheel={
            version:"3.1.12",
            setup:function(){
                if(this.addEventListener)for(var c=h.length;c;)this.addEventListener(h[--c],b,!1);else this.onmousewheel=b;
                a.data(this,"mousewheel-line-height",
                k.getLineHeight(this)),
                a.data(this,"mousewheel-page-height",
                k.getPageHeight(this))
            },
            teardown:function(){
                if(this.removeEventListener)for(var c=h.length;c;)this.removeEventListener(h[--c],b,!1);
                else this.onmousewheel=null;a.removeData(this,"mousewheel-line-height"),a.removeData(this,"mousewheel-page-height")
            },
            getLineHeight:function(b){
                var c=a(b),d=c["offsetParent"in a.fn?"offsetParent":"parent"]();
                return d.length||(d=a("body")),parseInt(d.css("fontSize"),10)||parseInt(c.css("fontSize"),10)||16
            },
            getPageHeight:function(b){
                return a(b).height();
            },
            settings:{
                adjustOldDeltas:!0,normalizeOffset:!0
            }
        };
        a.fn.extend({
            mousewheel:function(a){
                return a?this.bind("mousewheel",a):this.trigger("mousewheel")},
            unmousewheel:function(a){
                return this.unbind("mousewheel",a)
            }
        })
    });
    
    var isChrome = /Chrome/.test(navigator.userAgent) && /Google Inc/.test(navigator.vendor);
    if (!isChrome){
        $('#iframeAudio').remove()
    }
    else {
        $('#playAudio').remove() // just to make sure that it will not have 2x audio in the background 
    }
        
    $(function(){
        var i=0;
        var $btn = $('.section-btn li'),
            $wrap = $('.section-wrap'),
            $arrow = $('.arrow');
        
        function up(){
            i++;
            if(i==$btn.length){
                i=0
            };
        }
        function down(){
            i--;
            if(i<0){
                i=$btn.length-1
            };
        }
        
        function run(){
            $btn.eq(i).addClass('on').siblings().removeClass('on');	
            $wrap.attr("class","section-wrap")
                .addClass(function() { 
                    return "put-section-"+i; 
                })
                .find('.section')
                .eq(i)
                .find('.title')
                .addClass('active');
        };
        
        $btn.each(function(index) {
            $(this).click(function(){
                i=index;
                run();
            })
        });
        
        $arrow.one('click',go);
        function go(){
            up();
            run();	
            setTimeout(function(){
                $arrow.one('click',go)
            },1000);
        };
        
        $wrap.one('mousewheel', mouse_);
        function mouse_(event){
            if(event.deltaY < 0) {
                up();
            } else{
                down();
            }
            run();
            setTimeout(function(){
                $wrap.one('mousewheel',mouse_)
            },1000)
        };
        
        $(document).one('keydown',k);
        function k(event){
            var e=event||window.event;
            var key=e.keyCode||e.which||e.charCode;
            switch(key)	{
                case 38: down();run();	
                break;
                case 40: up();run();	
                break;
            };
            setTimeout(function(){
                $(document).one('keydown',k)
            },1000);
        }
    });
}

function getQueryParams(qs) {
    qs = qs.split('+').join(' ');

    var params = {},
        tokens,
        re = /[?&]?([^=]+)=([^&]*)/g;

    while (tokens = re.exec(qs)) {
        params[decodeURIComponent(tokens[1])] = decodeURIComponent(tokens[2]);
    }

    return params;
}

function isElementInViewport(el) {
    // special bonus for those using jQuery
    if (typeof jQuery === "function" && el instanceof jQuery) {
    el = el[0];
    }
    var rect = el.getBoundingClientRect();
    return (
    (rect.top <= 0
        && rect.bottom >= 0)
    ||
    (rect.bottom >= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.top <= (window.innerHeight || document.documentElement.clientHeight))
    ||
    (rect.top >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight))
    );
}

