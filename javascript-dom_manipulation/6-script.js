fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then((data) => {
    const characterElement = document.getElementById('character');
    characterElement.textContent = data.name;
  })
  .catch((error) => {
    console.error('Fetch failed', error);
  });