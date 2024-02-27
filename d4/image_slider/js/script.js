var i = 0;
var img = document.getElementById("img");

var array = ["1.png", "2.png", "3.png", "4.png", "5.png"];
img.src = "1.png";

function nextImg() {
    i++;
    img.src = array[i];
}

function previousImg() {
    i--;
    img.src = array[i];
}