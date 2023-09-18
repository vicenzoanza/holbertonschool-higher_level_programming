const change = document.querySelector('header');
const toggle = document.getElementById('toggle_header');

toggle.addEventListener('click', function onClick () {
  change.classList.toggle('green');
  change.classList.toggle('red');
});