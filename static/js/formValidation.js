var today = new Date();
var dd = String(today.getDate()).padStart(2, '0');
var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
var yyyy = today.getFullYear();

today = yyyy + '-' + mm + '-' + dd;

$('#id_datefrom').attr('min',today)
$('#id_dateto').attr('min',today) 



$(document).ready(function(){

    var required_fields = $('#addTourForm').find('input[required],textarea[required]')


    function checkTourFormValidation(){
        required_fields = $('#addTourForm').find('input[required],textarea[required]')

        var empty_fields = []
        for (var index = 0; index < required_fields.length; index++) {
            var required_field = $(required_fields[index])
            if(required_field.val() == ''){
                
                var result = {
                    valid : false,
                    empty_field : required_field.attr('name')
                }
                return result
            }
        }
        return {valid : true}
    }

    $('#formControlMenu li').click(function(e){
    var form_result = checkTourFormValidation()
    console.log(required_fields);
    if(form_result.valid){
        $('#save-tour-btn').css('display','none')
        $('#save-tour-submit').css('display','block')
    }else{
        console.log($('#formMessageBox'));
        $('#formMessageBox')[0].innerHTML = `<p>You didn't enter <span style="color:red;font-weight:bold; font-size:15px;">Trip ${form_result.empty_field}</span>. Please, go back and check informations.</p>`
    }
    })

    $('#addTourForm .next_btn').click(function(e){
        var form_result = checkTourFormValidation()
        if(form_result.valid){
            $('#save-tour-btn').css('display','none')
            $('#save-tour-submit').css('display','block')
        }else{
            console.log($('#formMessageBox'));
            $('#formMessageBox')[0].innerHTML = `<p>You didn't enter <span style="color:red;font-weight:bold; font-size:15px;">Trip ${form_result.empty_field}</span>. Please, go back and check informations.</p>`
        }
    })

})

