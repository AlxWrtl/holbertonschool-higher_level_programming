-- Retrieve the 'score' and 'name' columns from 'second_table' for rows where 'score' is greater than or equal to 10
-- Order the results by the 'score' column in descending order
SELECT
    score,
    name
FROM
    second_table
WHERE
    score >= 10
ORDER BY
    score DESC;