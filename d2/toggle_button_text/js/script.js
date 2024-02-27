const btn = document.getElementById('btn');

btn.addEventListener('click', function handleClick() {
    const initialText = 'Hello!';
  
    if (btn.textContent.toLowerCase().includes(initialText.toLowerCase())) {
      btn.textContent = 'Goodbye!';
    } else {
      btn.textContent = initialText;
    }
  });