imgdiv = document.querySelectorAll("#images p")
for(let i=1; i<imgdiv.length; i++){
    imgdiv[i].style.display = "none"
}
imgcount = 1
function addimg(){
    imgdiv[imgcount].style.display = "block"
    imgcount++
}


detaildiv = document.querySelectorAll("#details p")
for(let i=2; i<detaildiv.length; i++){
    detaildiv[i].style.display = "none"
}
detailcount = 2
function adddetail(){
    detaildiv[detailcount].style.display = "block"
    detaildiv[detailcount+1].style.display = "block"
    detailcount+=2
}


schedulediv = document.querySelectorAll("#schedules p")
for(let i=1; i<schedulediv.length; i++){
    schedulediv[i].style.display = "none"
}
schedulecount = 1
function addschedule(){
    schedulediv[schedulecount].style.display = "block"
    schedulecount++
}