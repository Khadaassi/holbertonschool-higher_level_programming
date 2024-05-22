const addItemButton = document.getElementById('add_item');

addItemButton.addEventListener('click', function () {
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';

  const myList = document.querySelector('.my_list');

  myList.appendChild(newItem);
});