-- Create a new table named 'second_table' if it does not already exist
-- The table includes three columns: 'id' as an integer, 'name' as a VARCHAR(256), and 'score' as an integer
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);

-- Insert multiple rows into 'second_table' with specified values for 'id', 'name', and 'score'
INSERT INTO second_table (id, name, score)
VALUES
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Jhon', 14),
    (4, 'George', 8);
