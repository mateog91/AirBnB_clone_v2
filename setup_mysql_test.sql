-- Script that prepares a MySQL server for the project
-- Create database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create new user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant privileges on hbnb_test_db database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Grant only select privilege on performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
