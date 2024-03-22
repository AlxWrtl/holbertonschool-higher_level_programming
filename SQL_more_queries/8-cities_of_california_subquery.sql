-- Retrieve the 'id' and 'name' columns from the 'cities' table for cities located in the state of 'California'
-- It uses a subquery to find the 'id' of 'California' in the 'states' table to match the 'state_id' in the 'cities' table
-- Results are ordered by 'id' in ascending order
SELECT
    id,
    name
FROM
    cities
WHERE
    cities.state_id = (
        SELECT
            id
        FROM
            states
        WHERE
            name = 'California'
    )
ORDER BY
    id ASC;