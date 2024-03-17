-- creates a table second_table in the database 

CREATE TABLE IF NOT EXIST second_table (
    id INT,
    name VARCHAR(256),
    score INT
    );

-- create these records into the 'second_table'
INSERT INTO second_table (id, name, score) VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);
