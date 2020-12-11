-- SQL - More queries 
-- creates the MySQL server user user_0d_1
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states   (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMERY KEY,
    name VARCHAR(256) NOT NULL
);