-- Calculate the number of TV shows for each genre and order the result by the number of shows in descending order
-- This query joins 'tv_genres' with 'tv_show_genres' where the 'id' in 'tv_genres' matches the 'genre_id' in 'tv_show_genres'
-- It groups the results by the genre name, counts the number of shows per genre, and orders the results by this count in descending order
SELECT
    tv_genres.name AS genre,
    COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM
    tv_genres
    INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY
    tv_genres.name
ORDER BY
    number_of_shows DESC;