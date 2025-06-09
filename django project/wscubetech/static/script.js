// script.js
document.addEventListener('DOMContentLoaded', function () {
    console.log('Document loaded');

    // Function to handle button click
    function handleClick() {
        alert("Button clicked!");
    }

    // Add event listener to button
    var button = document.getElementById("clickMeButton");
    button.addEventListener("Click Here", handleClick);
});
