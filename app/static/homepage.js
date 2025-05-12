document.addEventListener("DOMContentLoaded", function () {
    const buttons = document.querySelectorAll(".store-button");
    const allItems = ['Juice', 'Bananas', 'Milk', 'Eggs', 'Jam', 'Chips', 'Soda'];
    let allViewedBefore = false;

    // always attach this at the start, so it's available no matter when the modal shows
    const quizBtn = document.getElementById('goToQuizBtn');
    if (quizBtn) {
        quizBtn.addEventListener('click', function () {
            window.location.href = '/quiz-intro';
        });
    }


    // Function to check if all items are viewed
    function checkAllItemsViewed() {
        console.log("Checking if all items viewed...");

        const allViewedNow = allItems.every(item => {
            return sessionStorage.getItem(item) === 'true';
        });
    
        // Only show modal ONCE, and ONLY after all buttons have been clicked
        if (allViewedNow && !localStorage.getItem("readyModalShown")) {
            // Show the modal
            const readyToShopModal = new bootstrap.Modal(document.getElementById('readyToShopModal'));
            readyToShopModal.show();

            // Mark modal shown once
            sessionStorage.setItem("readyModalShown", "1");
            console.log("ALL ITEMS VIEWED: showing modal (first time)");
        }
    }    
    

    buttons.forEach(button => {
        const id = button.dataset.item;

        // Function to update styles to gray
        const setToGray = () => {
            button.style.color = "#b0b0b0";
            button.style.borderColor = "#b0b0b0";
        };

        // On page load: check if the button was clicked before
        if (sessionStorage.getItem(id) === 'true') {
            setToGray();
        }

        // On click: store and update styles
        button.addEventListener("click", () => {
            sessionStorage.setItem(id, 'true');
            setToGray();
            
            // Check if all items are viewed after each click
            checkAllItemsViewed();
        });
    });

    // Existing first visit modal logic
    if (!localStorage.getItem("hasVisited")) {
        var myModal = new bootstrap.Modal(document.getElementById('howToModal'), {
            keyboard: false
        });
        myModal.show();
        localStorage.setItem("hasVisited", "true");
    }

    // Show the modal if coming from landing page
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.has('showModal')) {
        var myModal = new bootstrap.Modal(document.getElementById('howToModal'), {
            keyboard: false
        });
        myModal.show();
    }

    // If modal was already shown once, show it again (only once more)
    if (sessionStorage.getItem("readyModalShown") === "1") {
        const readyToShopModal = new bootstrap.Modal(document.getElementById('readyToShopModal'));
        readyToShopModal.show();
        sessionStorage.setItem("readyModalShown", "2");
        console.log("ALL ITEMS VIEWED: showing modal (second time)");
    }

});