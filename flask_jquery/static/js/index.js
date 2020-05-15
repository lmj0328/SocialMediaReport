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

    $('#explore-project').click(function() {
        $('#backdrop').removeClass('hidden');
        $('#user-input-form').removeClass('hidden');
        $('html').addClass('disable-scroll');
    });


    $('#cross-btn').click(function() {
        $('#backdrop').addClass('hidden');
        $('#user-input-form').addClass('hidden');
        $('html').removeClass('disable-scroll');
    });


    // $(document).ready(function() {
    //     $('#get-report').click('submit', function(event) {
    //         $.ajax({
    //             url: '/report',
    //             data: $('form').serializeArray(),
    //             type: 'POST',
    //             success: function(response) {
    //                 loading();
    //                 // $('#response').text(JSON.stringify(response));
    //             }
    //         })
    //     });
    // });
}


function loading() {
    $('#user-input-form').addClass('hidden');
    $('#spinner').removeClass('hidden');
    console.log("hide input, show spinner");
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

