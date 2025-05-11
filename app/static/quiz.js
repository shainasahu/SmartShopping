document.addEventListener('DOMContentLoaded', function() {
  // Timer functionality
  let timer = 10;
  const timerElement = document.getElementById('timer');
  let countdown = setInterval(updateTimer, 1000);

  function updateTimer() {
      timer--;
      timerElement.textContent = timer;
      if (timer <= 0) {
          clearInterval(countdown);
          handleTimeUp();
      }
  }

// =============================================

const hintContainer = document.querySelector('.hint-container'); // 🔧 Changed this line
const hintLink = document.querySelector('.hint-link');
const hintText = document.getElementById('hint-text');

if (hintLink && hintText && hintContainer) {
    let hoverTimeout;
    let isHintVisible = false;

    // ✅ FIX: Listen for mouseenter/leave on the whole container to avoid flickering
    hintContainer.addEventListener('mouseenter', () => {
        clearTimeout(hoverTimeout);
        if (!isHintVisible) {
            hintText.style.opacity = '0';
            hintText.style.display = 'block';
            setTimeout(() => {
                hintText.style.opacity = '1';
            }, 10);
            isHintVisible = true;
        }
    });

    hintContainer.addEventListener('mouseleave', () => {
        clearTimeout(hoverTimeout);
        hoverTimeout = setTimeout(() => {
            hintText.style.opacity = '0';
            setTimeout(() => {
                hintText.style.display = 'none';
            }, 200);
            isHintVisible = false;
        }, 200);
    });

    // Mobile/touch click toggle stays same
    hintLink.addEventListener('click', (e) => {
        e.preventDefault();
        clearTimeout(hoverTimeout);
        if (isHintVisible) {
            hintText.style.opacity = '0';
            setTimeout(() => {
                hintText.style.display = 'none';
            }, 200);
        } else {
            hintText.style.opacity = '0';
            hintText.style.display = 'block';
            setTimeout(() => {
                hintText.style.opacity = '1';
            }, 10);
        }
        isHintVisible = !isHintVisible;
    });

    hintText.addEventListener('mousedown', (e) => {
        e.preventDefault();
    });

    hintText.style.display = 'none';
    hintText.style.transition = 'opacity 0.2s ease';
}
// =============================================

        

  // Button click handlers
  const priceButtons = document.querySelectorAll('.price-btn');
  priceButtons.forEach(button => {
      button.addEventListener('click', function(e) {
          e.preventDefault();
          handleChoice(this.value, this.dataset.correct, this.dataset.tactic);
      });
  });

  // Continue button handler
  const continueBtn = document.getElementById('continue-btn');
  if (continueBtn) {
      continueBtn.addEventListener('click', submitForm);
  }

  function handleTimeUp() {
      const firstButton = document.querySelector('.price-btn');
      if (firstButton) {
          handleChoice('', firstButton.dataset.correct, firstButton.dataset.tactic);
      }
  }

  function handleChoice(selected, correct, tactic) {
      clearInterval(countdown);
      if (timerElement) timerElement.style.display = 'none';

      const feedbackBox = document.getElementById("feedback-box");
      const feedbackMessage = document.getElementById("feedback-message");
      
      if (feedbackBox && feedbackMessage) {
          let message = "";
          
          if (selected === correct) {
              message = `<h4>✅ Correct!</h4>The best value was: <h4>${correct}</h4><strong>Remember, </strong>${tactic}<br><br>`;
          } else if (selected === "") {
              message = `<h4>⏰ Time's up!</h4>The more expensive item will be automatically added to your cart.<br>The best value was: <h4>${correct}</h4><strong>Remember, </strong>${tactic}<br><br>`;
          } else {
              message = `<h4>❌ Incorrect.</h4>The best value was: <h4>${correct}</h4><strong>Remember, </strong>${tactic}<br><br>`;
          }

          feedbackMessage.innerHTML = message;
          feedbackBox.classList.remove("hidden");
      }

      // Disable all buttons
      priceButtons.forEach(btn => {
          if (btn) btn.disabled = true;
      });
  }

  function submitForm() {
      const form = document.getElementById("quiz-form");
      if (form) {
          const selectedOption = document.querySelector('.price-btn[disabled]');
          const selectedValue = selectedOption ? selectedOption.value : '';
          
          const hiddenInput = document.createElement("input");
          hiddenInput.type = "hidden";
          hiddenInput.name = "selected_price";
          hiddenInput.value = selectedValue;
          form.appendChild(hiddenInput);
          form.submit();
      }
  }
});