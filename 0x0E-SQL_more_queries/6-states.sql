-- creates database hbtn_0d_usa and table states

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE states(PRIMARY KEY(id), id INT UNIQUE AUTO_INCREMENT NOT NULL, name VARCHAR (256) NOT NULL);
