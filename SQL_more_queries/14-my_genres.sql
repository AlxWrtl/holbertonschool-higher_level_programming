-- Retrieve the genres associated with the TV show 'Dexter'
-- This query joins 'tv_genres' with 'tv_show_genres', and then 'tv_show_genres' with 'tv_shows' to filter shows by title
-- The results are ordered by the genre name in ascending order
SELECT
    tv_genres.name
FROM
    tv_genres
    INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
    INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE
    tv_shows.title = 'Dexter'
ORDER BY
    tv_genres.name ASC;