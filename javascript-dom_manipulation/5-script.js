const header = document.querySelector('header');
const update = document.getElementById('update_header');

update.addEventListener('click', function onClick () {
  header.textContent = 'New Header!!!';
});