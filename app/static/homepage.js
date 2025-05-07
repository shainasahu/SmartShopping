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

    // functionality to show modal on first visit
    if (!localStorage.getItem("hasVisited")) {
        // Show the modal if it's the first visit
        var myModal = new bootstrap.Modal(document.getElementById('howToModal'), {
            keyboard: false // Optionally disable closing with the keyboard
        });
        myModal.show();

        // Set a flag in localStorage so the modal won't show again
        localStorage.setItem("hasVisited", "true");
    }

    // Show the modal if the user is coming from the landing page (via query parameter)
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.has('showModal')) {
        var myModal = new bootstrap.Modal(document.getElementById('howToModal'), {
            keyboard: false // Optionally disable closing with the keyboard
        });
        myModal.show();
    }
});