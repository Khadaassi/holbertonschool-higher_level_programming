const header = document.querySelector('header');
const toggleHeader = document.getElementById('toggle_header');

toggleHeader.addEventListener('click', function () {
  header.classList.toggle('red');
  header.classList.toggle('green');
});