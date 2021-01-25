var photo_box = $('#photo-form-box').children('.photo-item')
var photo_count = 1
// console.log(photo_box);

for(let i=1; i<photo_box.length; i++){
    $(photo_box[i]).css('visibility','hidden')
}

function addPhoto(){
    $(photo_box[photo_count]).css('visibility','unset')
    photo_count++
}

var schedule_box = $('#schedule-form-box').children('.photo-item')
// console.log(schedule_box);
var schedule_count = 1

for(let i=1; i<schedule_box.length; i++){
    $(schedule_box[i]).css('visibility','hidden')
}

function addSchedule(){
    $(schedule_box[schedule_count]).css('visibility','unset')
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
    $(url_box[i]).css('visibility','hidden')
}

function addurl(){
    $(url_box[url_count]).css('visibility','unset')
    url_count++
}


$('#formControlMenu li').click(function(){
    // console.log($(this).data('target'));
    $('#formControlMenu li').removeClass('active')
    $(this).addClass('active')
    $('#addTourForm').children().hide()
    $('#addTourForm').children(`#${$(this).data('target')}`).show()
    $('#organizerActions').children().hide()
    $('#organizerActions').children(`#${$(this).data('target')}`).show()         

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


  $('.help-btn').click(function(){
      $('.help-text').toggle()
  })


  $('#id_map_link').change(function(){
    var iframe_src = $($(this).val()).attr('src')
    if (iframe_src){
        $('input[name="map_link"]').val(iframe_src)
        $('#iframe-link-box').slideDown(200)
    }else{
        $('input[name="map_link"]').val('')
        alert("We couldn't get link, please enter correct item.")
    }
    
})

$('#trip_date').change(function(e){
    if(e.target.value == 'all_year'){
        var answer = confirm('All Year Availability. This will hide dates from your tour.')
        if(answer){
            $('#start-end-date-box').hide(200)
        }else{
            $($('#trip_date').children()[0]).removeAttr('selected');
            $($('#trip_date').children()[0]).attr('selected','true');
        }
        
    }
    else if(e.target.value == 'one_time'){
        $('#start-end-date-box').show(200)
    }
})

var btn_right_position = $('#organizer-menu-btn').css('right') 
console.log(btn_right_position);
$('#organizer-menu-btn').click(function(){
    if ($(window).width() < 972) {
        console.log('okk');
        $('#org-menu-nav').toggle()
        $('#org-menu-nav').find('span').toggle(100)
    }
    else{
        $('#org-menu-nav').find('span').toggle(100)
    }
   
   
//    $('#organizer-menu-btn').find('i').css({
//         transform: 'rotate(180deg)'
//     });
})

var org_menu_a_list = $('#org-menu-nav').find('li')
// $(org_menu_a_list).hover(function(){
//     $('#org-menu-nav').find('span').show(100)
// }, function(){
//     $('#org-menu-nav').find('span').hide(100)
// })

var degree = 180
$('.form-steps-btn').click(function(){
    $('.tour-menu-list-nav').slideToggle(200)
    
    if(degree == 180){
        $('.fa-chevron-down').css({
            'transform' : `rotate(${degree}deg)`
        })
        degree = 0
    }
    else{
        $('.fa-chevron-down').css({
            'transform' : `rotate(${degree}deg)`
        })
        degree = 180
    }
    
})