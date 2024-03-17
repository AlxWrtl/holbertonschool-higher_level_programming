-- Creates a table named 'second_table' if it does not exist with columns 'id' (INT), 'name' (VARCHAR(256)), and 'score' (INT)
CREATE TABLE
    IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);

-- Inserts a row into 'second_table' with id = 1, name = 'John', and score = 10
INSERT INTO
    second_table
SET
    id = 1,
    name = 'John',
    score = 10;

-- Inserts a row into 'second_table' with id = 2, name = 'Alex', and score = 3
INSERT INTO
    second_table
SET
    id = 2,
    name = 'Alex',
    score = 3;

-- Inserts a row into 'second_table' with id = 3, name = 'Bob', and score = 14
INSERT INTO
    second_table
SET
    id = 3,
    name = 'Bob',
    score = 14;

-- Inserts a row into 'second_table' with id = 4, name = 'George', and score = 8
INSERT INTO
    second_table
SET
    id = 4,
    name = 'George',
    score = 8;