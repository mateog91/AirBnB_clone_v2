-- Script that prepares a MySQL server for the project
-- Create database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create new user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant privileges on hbnb_dev_db database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Grant only select privilege on performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
