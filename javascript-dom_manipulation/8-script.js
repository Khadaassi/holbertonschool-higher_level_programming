fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then(response => response.json())
  .then((data) => {
    const helloElement = document.getElementById('hello');
    helloElement.textContent = data.hello;
  })
  .catch((error) => {
    console.error('Fetch failed', error);
  });