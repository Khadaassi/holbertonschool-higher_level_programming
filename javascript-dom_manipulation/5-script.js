const updateHeaderButton = document.getElementById('update_header');

updateHeaderButton.addEventListener('click', function () {
  const header = document.querySelector('header');
  header.textContent = 'New Header!!!';
});