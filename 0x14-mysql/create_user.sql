DROP USER IF EXISTS 'holberton_user'@'localhost';
DROP USER IF EXISTS 'replica_user'@'localhost';

CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *. * TO 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';

DROP DATABASE IF EXISTS tyrell_corp;
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);
INSERT INTO nexus6 (name) VALUES ("Tyrell Jr.");
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';


CREATE USER 'replica_user'@'%' IDENTIFIED BY 'password';
GRANT REPLICATION SLAVE, REPLICATION CLIENT ON *. * TO 'replica_user'@'%';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';

FLUSH PRIVILEGES;
