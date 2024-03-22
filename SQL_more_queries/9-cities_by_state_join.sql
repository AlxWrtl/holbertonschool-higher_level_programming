-- Retrieve the 'id' and 'name' of cities along with the name of their corresponding state
-- This query joins the 'cities' table with the 'states' table based on the 'state_id' from 'cities' matching the 'id' in 'states'
-- Results are ordered by the 'id' of cities in ascending order
SELECT
    cities.id,
    cities.name,
    states.name
FROM
    cities
    JOIN states ON cities.state_id = states.id
ORDER BY
    cities.id ASC;