// email = document.querySelector('input[type=email]')
// password = document.querySelectorAll('input[type=password]')

// email.value = ""
// password.value = "asd"



images = document.querySelectorAll("#images p")
for(let i=1; i<images.length; i++){
    images[i].style.display = "none"
}
count = 1
function addimage(){
    images[count].style.display = "block"
    count++ 
}

schedules = document.querySelectorAll("#schedules p")
for(let i=1; i<schedules.length; i++){
    schedules[i].style.display = "none"
}
count3 = 1
function addschedule(){
    schedules[count3].style.display = "block"
    count3++
}

details = document.querySelectorAll("#details p")
for(let i=2; i<details.length; i++){
    details[i].style.display = "none"
}
count2 = 2
function adddetail(){
    details[count2].style.display = "block"
    details[count2+1].style.display = "block"
    count2+=2
}

// imagenum = 0
// for(let i=0; i<images.length; i++){
//     if(images[i].value != ""){
//         imagenum++
//     }
// }
// document.querySelector("#nums #imagenum").value = imagenum

// detailnum = 0
// for(let i=0; i<details.length; i++){
//     if(details[i].value != "No file chosen"){
//         detailnum++
//     }
// }
// document.querySelector("#nums #detailnum").value = detailnum

// schedulenum = 0
// for(let i=0; i<schedules.length; i++){
//     if(schedules[i].value != null){
//         schedulenum++
//     }
// }
// document.querySelector("#nums #schedulenum").value = schedulenum

// console.log(imagenum)
// console.log(detailnum)
// console.log(schedulenum)
// console.log(images[0].value)
// console.log(images[1].value)