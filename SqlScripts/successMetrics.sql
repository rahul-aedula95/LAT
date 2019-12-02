create database successMetrics;
use successMetrics;

CREATE TABLE IF NOT EXISTS status (
    id INT  NOT NULL,
    app_status VARCHAR(255) NOT NULL
   ) ;
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost';
GRANT ALL PRIVILEGES ON * . * TO 'TESTUSER'@'localhost' IDENTIFIED BY 'Pass_123';

FLUSH PRIVILEGES;
