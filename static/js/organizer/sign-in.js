function CheckPass(){
    var pass1 = document.getElementById('pass1');
    var pass2 = document.getElementById('pass2');
    var ErrorMessage = document.getElementById('pass-message');

    if( pass1.value.length < 6 ){
        ErrorMessage.style.display = "block";
    }
    else{
        ErrorMessage.style.display = "none"; 
    }
}


function openForm(){
    document.getElementById("pop-up-form").style.display = "block";
}

function closeForm(){
    document.getElementById("pop-up-form").style.display = "none";
}
    window.onclick = function(event) {
    var modal = document.getElementById('pop-up-form');
    if (event.target == modal) {
        closeForm();
    }
}