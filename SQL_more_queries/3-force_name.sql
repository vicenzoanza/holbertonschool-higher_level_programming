-- script that creates the table force_name on your MySQL server.
CREATE TABLE IF NOT EXISTS force_name (
    id int,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);