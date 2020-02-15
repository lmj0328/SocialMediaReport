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
