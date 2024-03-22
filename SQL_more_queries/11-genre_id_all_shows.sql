-- Retrieve the title of TV shows and their associated genre IDs, including shows that may not have a genre assigned
-- This query uses a LEFT JOIN to include all shows from 'tv_shows', even if they don't have an entry in 'tv_show_genres'
-- Results are ordered first by the title of the TV shows in ascending order and then by their genre IDs in ascending order
SELECT
    tv_shows.title,
    tv_show_genres.genre_id
FROM
    tv_shows
    LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY
    tv_shows.title ASC,
    tv_show_genres.genre_id ASC;