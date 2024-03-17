-- Retrieve the 'score' and the count of occurrences of each 'score' in 'second_table'
-- Group the results by the 'score' column
SELECT
    score,
    COUNT(*) AS number
FROM
    second_table
GROUP BY
    score;