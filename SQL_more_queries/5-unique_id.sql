-- Create a new table named 'unique_id' if it does not already exist
-- The table includes two columns: 'id' as an integer with a default value of 1 and marked as UNIQUE, and 'name' as a VARCHAR(256)
CREATE TABLE
    IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));