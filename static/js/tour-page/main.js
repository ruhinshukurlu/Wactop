$('.owl-carousel').owlCarousel({
    loop: true,
    nav: true,
    dots: false,
    items : 1
    
})
var count=0;
function change()
{
document.getElementById("like").innerHTML=++count;

}
function myFunc(){
    var dots = document.getElementById("dots"),
   moreText = document.getElementById("more"),
   btnText = document.getElementById("read-more-btn"),
   hope = document.querySelector(".hope");

  if (dots.style.display === "none") {
    dots.style.display = "inline";
    btnText.innerHTML = "Read more"; 
    moreText.style.display = "none";
  } else {
    dots.style.display = "none";
    btnText.style.display="none"; 
    moreText.style.display = "inline";
    hope.style.opacity = "1"

    
  }
}
// menu design
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

// back to top
function topFunction() {
            document.body.scrollTop = 0;
            document.documentElement.scrollTop = 0;
        }