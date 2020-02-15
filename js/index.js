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
})