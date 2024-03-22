-- Retrieve the title of TV shows and their associated genre IDs
-- This query joins the 'tv_shows' table with the 'tv_show_genres' table where the 'id' of the show matches the 'show_id' in 'tv_show_genres'
-- Results are ordered first by the title of the TV shows in ascending order and then by their genre IDs
SELECT
    tv_shows.title,
    tv_show_genres.genre_id
FROM
    tv_shows
    JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY
    tv_shows.title ASC,
    tv_show_genres.genre_id;