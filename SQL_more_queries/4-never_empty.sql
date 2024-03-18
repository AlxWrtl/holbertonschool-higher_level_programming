-- Create a new table named 'id_not_null' if it does not already exist
-- The table includes two columns: 'id' as an integer with a default value of 1, and 'name' as a VARCHAR(256)
CREATE TABLE
    IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));