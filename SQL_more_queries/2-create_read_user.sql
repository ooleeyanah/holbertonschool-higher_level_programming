-- create database and user
CREATE DATABASE hbtn_0d_2;
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON *.* TO 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';