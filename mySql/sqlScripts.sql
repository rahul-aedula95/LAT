create database successMetrics;
use successMetrics;

CREATE TABLE IF NOT EXISTS status (
    id INT  NOT NULL,
    app_status VARCHAR(255) NOT NULL
   ) ;

create database failureMetrics;
use failureMetrics;

CREATE TABLE IF NOT EXISTS failure (
    id INT  NOT NULL,
    app_status VARCHAR(255) NOT NULL
      ) ;

use mysql;
/*for every read processor*/
CREATE USER 'readprocessor1'@'10.138.15.197' IDENTIFIED BY 'Pass_123';

GRANT ALL PRIVILEGES ON * . * TO 'readprocessor1'@'10.138.15.197';
FLUSH PRIVILEGES;

use mysql;
/*for every read processor*/
CREATE USER 'readprocessor2'@'10.138.15.207' IDENTIFIED BY 'Pass_123';

GRANT ALL PRIVILEGES ON * . * TO 'readprocessor2'@'10.138.15.207';
FLUSH PRIVILEGES;

use mysql;

CREATE USER 'restproject'@'10.138.15.200' IDENTIFIED BY 'Pass_123';

GRANT ALL PRIVILEGES ON * . * TO 'restproject'@'10.138.15.200';
FLUSH PRIVILEGES;
