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