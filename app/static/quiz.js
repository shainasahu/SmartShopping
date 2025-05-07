function showHint() {
    document.getElementById('hint-text').classList.remove('hidden');
  }
  
  function hideHint() {
    document.getElementById('hint-text').classList.add('hidden');
  }
  
  let timer = 10;
  const countdown = setInterval(() => {
    timer--;
    document.getElementById('timer').innerText = timer;
    if (timer <= 0) {
      document.querySelector('form').submit();
      clearInterval(countdown);
    }
  }, 1000);

  function handleChoice(selected, correct, tactic) {
    let message = "";
    if (selected === correct) {
      message = `✅ Correct!\nYou chose the better price.\nTactic used: ${tactic}`;
    } else {
      message = `❌ Incorrect.\nThe better price was ${correct}.\nTactic used: ${tactic}`;
    }
  
    alert(message);
  
    // After alert, submit the answer
    const form = document.querySelector("form");
    const hiddenInput = document.createElement("input");
    hiddenInput.type = "hidden";
    hiddenInput.name = "selected_price";
    hiddenInput.value = selected;
    form.appendChild(hiddenInput);
    form.submit();
  }
  