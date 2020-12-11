-- SQL - More queries 
-- creates the MySQL server user user_0d_1
CREATE TABLE IF NOT EXISTS unique_id   (
    id INT DEFAULT 1,
    name VARCHAR(256),
    UNIQUE KEY (id)
)