-- Create the database 'hbtn_0d_usa' if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Select the 'hbtn_0d_usa' database for use
USE hbtn_0d_usa;

-- Create the table 'cities' within the 'hbtn_0d_usa' database if it does not exist
-- The table includes an 'id' column that is an integer, not null, auto-increments, and is the primary key
-- It includes a 'state_id' column that must not be null and establishes a foreign key relationship with the 'states' table's 'id' column
-- It also includes a 'name' column that is a VARCHAR(256) and cannot be null
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states (id)
);
