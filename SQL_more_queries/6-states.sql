-- create a bit more detailed table
USE @hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa(
id INT NOT NULL UNIQUE,
name VARCHAR(256) NOT NULL,
PRIMARY KEY (id)
);