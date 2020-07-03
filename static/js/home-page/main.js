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
            items: 5
        }
    }
})
var modal = document.getElementById('login');

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
$('.menu-btn').click(function(){
    $('.menu-box-in').stop().animate({
        width : 'toggle'
    },500);
  });
  
  $('.menu-btn').click(function(){
    $('.menu-box').css("display","block");
    $('body').css("overflow","hidden");
  });
  $('.close-btn, .menu-box').click(function(){
    $('.menu-box').css("display","none");
    $('.menu-box-in').stop().animate({
        width : 'toggle'
    },500);
    $('body').css("overflow","auto");
  });

// end
