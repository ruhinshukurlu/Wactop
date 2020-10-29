$('.owl-carousel').owlCarousel({
    loop: true,
    nav: true,
    dots: false,
    items : 5
    
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
// main-menu  
$('.menu-btn').click(function(){
  $('.menu-box-in').stop().animate({
      width : 'toggle'
  },300);
});

$('.menu-btn').click(function(){
  $('.menu-box').css("display","block");
  $('body').css("overflow","hidden");
});
$('.close-btn, .menu-box').click(function(){
  $('.menu-box').css("display","none");
  $('.menu-box-in').stop().animate({
      width : 'toggle'
  },300);
  $('body').css("overflow","auto");
});

// back to top
function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}

function readURL1(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#cover').attr('src', e.target.result);
        }

        reader.readAsDataURL(input.files[0]);
    }
}

$("#coverimgInp").change(function(){
    readURL1(this);
});

function readURL2(input) {
  if (input.files && input.files[0]) {
      var reader = new FileReader();

      reader.onload = function (e) {
          $('#profile').attr('src', e.target.result);
      }

      reader.readAsDataURL(input.files[0]);
  }
}

$("#profileimgInp").change(function(){
  readURL2(this);
});
