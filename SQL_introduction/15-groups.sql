-- List the number of records with the same score in the 'second_table' of the 'hbtn_0c_0' database
-- Display 'score' and the count of records for each score labeled as 'number'
-- Sort the list by the count of records (number) in descending order
SELECT
    score,
    COUNT(*) AS number
FROM
    second_table
GROUP BY
    score
ORDER BY
    number DESC;
