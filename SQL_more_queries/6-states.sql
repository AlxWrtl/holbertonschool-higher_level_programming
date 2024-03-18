-- Create the database 'hbtn_0d_usa' if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Select the 'hbtn_0d_usa' database for use
USE hbtn_0d_usa;

-- Create the table 'states' within the 'hbtn_0d_usa' database if it does not exist
-- The table includes an 'id' column that is an integer, not null, auto-increments, and is the primary key
-- It also includes a 'name' column that is a VARCHAR(256) and cannot be null
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);