-- Retrieve the 'score' and 'name' columns from 'second_table' for rows where 'name' is not NULL
-- Order the results by the 'score' column in descending order
SELECT
    score,
    name
FROM
    second_table
WHERE
    name IS NOT NULL
ORDER BY
    score DESC;