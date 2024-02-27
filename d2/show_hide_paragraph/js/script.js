const myButton = document.getElementById("myButton");
const myP = document.getElementById("myP");

myButton = addEventListener("click", event => {
    if(myP.style.display === "none") {
        myP.style.display = "block";
        myButton.textContent = "Hide";
    }
    else {
        myP.style.display = "none";
        myButton.textContent = "Show";
    }
});