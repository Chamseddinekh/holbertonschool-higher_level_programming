-- SQL - More queries 
-- creates the MySQL server user user_0d_1
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states   (
    PRIMERY KEY id INT NOT NULL AUTO_INCREMENtT,
    name VARCHAR(256) NOT NULL,
    UNIQUE KEY (id)
)