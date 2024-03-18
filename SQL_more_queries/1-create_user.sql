-- Create the user 'user_0d_1' for 'localhost' if it doesn't already exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Grant all privileges on all databases and tables to 'user_0d_1' at 'localhost'
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';