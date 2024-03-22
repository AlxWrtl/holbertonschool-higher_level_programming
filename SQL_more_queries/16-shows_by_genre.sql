-- Retrieve the titles of TV shows along with their associated genre names, if available
-- This query uses LEFT JOINs to include all shows from 'tv_shows', even those without an entry in 'tv_show_genres' or 'tv_genres'
-- Results are ordered first by the title of the TV shows in ascending order and then by the genre names in ascending order
SELECT
    tv_shows.title,
    tv_genres.name
FROM
    tv_shows
    LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY
    tv_shows.title ASC,
    tv_genres.name ASC;