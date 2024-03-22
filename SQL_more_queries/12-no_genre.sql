-- Retrieve the titles of TV shows that do not have an associated genre
-- This query uses a LEFT JOIN to include all shows from 'tv_shows' and then filters out those that have a genre by looking for NULL in 'tv_show_genres.show_id'
-- Results are ordered by the title of the TV shows in ascending order. The genre_id column will not have meaningful data due to the WHERE clause filtering for NULL show_id, implying these shows lack a genre
SELECT
    tv_shows.title,
    tv_show_genres.genre_id
FROM
    tv_shows
    LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE
    tv_show_genres.show_id IS NULL
ORDER BY
    tv_shows.title ASC;