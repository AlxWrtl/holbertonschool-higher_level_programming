-- Retrieve the titles of TV shows classified under the 'Comedy' genre
-- This query performs an inner join between 'tv_shows' and 'tv_show_genres', and then 'tv_show_genres' with 'tv_genres' to filter by genre name
-- The results are ordered by the show title in ascending order
SELECT
    tv_shows.title
FROM
    tv_shows
    INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE
    tv_genres.name = "Comedy"
ORDER BY
    tv_shows.title;