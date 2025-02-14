document.addEventListener("DOMContentLoaded", function () {
    const volunteerBtns = document.querySelectorAll(".btn");

    volunteerBtns.forEach((btn) => {
        btn.addEventListener("click", function (e) {
            if (e.target.getAttribute("href") === "#volunteer") {
                e.preventDefault();
                window.open("https://docs.google.com/forms/d/1nOQqpTvImOguJyxPbil9EQ6bHz62xOF58RensplIz5I/", "_blank");
            }
        });
    });
});