-- create a bit more detailed table
USE IF EXISTS @hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa(
id INT AUTO_INCREMENT NOT NULL,
name VARCHAR(256) NOT NULL,
PRIMARY KEY (id)
);