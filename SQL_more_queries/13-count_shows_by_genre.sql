-- Import the database dump from hbtn_0d_tvshows to your MySQL server
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = genre_id
GROUP BY tv_genres.genre
ORDER BY number_of_shows DESC;
