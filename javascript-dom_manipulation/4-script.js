    const add = document.getElementById('add_item');
    const lista = document.querySelector('.my_list');

    add.addEventListener('click', function () {
        const n_lista = document.createElement('li');
        n_lista.textContent = 'Item';
        lista.appendChild(n_lista);
  });