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

var paragraph_box_en = $('#text-forms-en').children('.form-group')
var paragraph_box_az = $('#text-forms-az').children('.form-group')
var paragraph_box_ru = $('#text-forms-ru').children('.form-group')

// console.log(paragraph_box);
var paragraph_count_en = 1
var paragraph_count_az = 1
var paragraph_count_ru = 1


for(let i=1; i<paragraph_box_en.length; i++){
    $(paragraph_box_en[i]).css('display','none')
    $(paragraph_box_az[i]).css('display','none')
    $(paragraph_box_ru[i]).css('display','none')
}

function adddetail_en(){
    $(paragraph_box_en[paragraph_count_en]).show()
    paragraph_count_en++
}

function adddetail_az(){
    $(paragraph_box_az[paragraph_count_az]).show()
    paragraph_count_az++
}

function adddetail_ru(){
    $(paragraph_box_ru[paragraph_count_ru]).show()
    paragraph_count_ru++
}

var url_box = $('#urls').children('.form-group')

var url_count = 3
for(let i=3; i<url_box.length; i++){
    $(url_box[i]).css('display','none')
}

function addurl(){
    $(url_box[url_count]).show()
    url_count++
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