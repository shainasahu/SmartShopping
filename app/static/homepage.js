document.addEventListener("DOMContentLoaded", function () {
    const buttons = document.querySelectorAll(".store-button");

    buttons.forEach(button => {
        const id = button.textContent.trim();

        // Function to update styles to gray
        const setToGray = () => {
            button.style.color = "#b0b0b0";
            button.style.borderColor = "#b0b0b0";
        };

        // On page load: check if the button was clicked before
        if (sessionStorage.getItem(id)) {
            setToGray();
        }

        // On click: store and update styles
        button.addEventListener("click", () => {
            sessionStorage.setItem(id, true);
            setToGray();
        });
    });
});