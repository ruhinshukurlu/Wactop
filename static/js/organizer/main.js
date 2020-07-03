
$(document).ready(function(){
    $('.mymenu').click(function(){
        $('.head-menu').slideToggle(500);
    });
});
    
$(document).ready(function(){
      

$('.owl-carousel').owlCarousel({
    loop: true,
    margin: 25,
    nav: true,
    dots: false,
    responsive: {
        1: {
            items: 1,
            dots: false
        },
        600: {
            items: 3
        },
        800: {
            items: 4
        },
        1000: {
            items: 4
        }
    }
});
});
