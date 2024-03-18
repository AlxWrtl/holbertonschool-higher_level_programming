-- Create a new table named 'force_name' if it does not already exist
-- The table includes two columns: 'id' as an integer and 'name' as a VARCHAR(256) that cannot be NULL
CREATE TABLE
    IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);