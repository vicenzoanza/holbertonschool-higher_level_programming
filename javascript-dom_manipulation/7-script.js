const movies = document.getElementById('list_movies');
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    data.results.forEach(element => {
        const lista = document.createElement('li');
        lista.textContent = element.title
        movies.appendChild(lista)
    });
  });