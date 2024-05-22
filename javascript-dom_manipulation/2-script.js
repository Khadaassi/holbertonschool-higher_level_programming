const redButton = document.querySelector('#red_header');

redButton.addEventListener('click', function () {
  document.querySelector('header').classList.add('red');
});