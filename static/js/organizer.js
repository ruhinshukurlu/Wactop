var photo_box = $('#photo-form-box').children('.photo-item')
var photo_count = 1
// console.log(photo_box);

for(let i=1; i<photo_box.length; i++){
    $(photo_box[i]).css('display','none')
}

function addPhoto(){
    $(photo_box[photo_count]).show()
    photo_count++
}

var schedule_box = $('#schedule-form-box').children('.photo-item')
// console.log(schedule_box);
var schedule_count = 1

for(let i=1; i<schedule_box.length; i++){
    $(schedule_box[i]).css('display','none')
}

function addSchedule(){
    $(schedule_box[schedule_count]).show()
    schedule_count++
}

var paragraph_box = $('#text-forms').children('.form-group')
// console.log(paragraph_box);
var paragraph_count = 1

for(let i=1; i<paragraph_box.length; i++){
    $(paragraph_box[i]).css('display','none')
}

function adddetail(){
    $(paragraph_box[paragraph_count]).show()
    paragraph_count++
}


$('#formControlMenu li').click(function(){
    // console.log($(this).data('target'));
    $('#addTourForm').children().hide()
    $('#addTourForm').children(`#${$(this).data('target')}`).show()          

})

$('.next_btn').click(function(){
    // console.log($(this).data('target'));
    $('#addTourForm').children().hide()
    $('#addTourForm').children(`#${$(this).data('target')}`).show()
})


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