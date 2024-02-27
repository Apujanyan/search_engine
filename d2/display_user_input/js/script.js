let userInput;

document.getElementById("myDisplay").onclick = function() {
    userInput = document.getElementById("myText").value;
    document.getElementById("myH1").textContent = userInput; 
}