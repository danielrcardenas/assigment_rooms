create user 'bigasdev'@'%' IDENTIFIED BY 'devel.2017';
create user 'bigasprod'@'%' IDENTIFIED BY 'prod.2017';
CREATE DATABASE bigasdb_dev DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
CREATE DATABASE bigasdb_prod DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
GRANT ALL PRIVILEGES ON bigasdb_dev.* TO 'bigasdev'@'%' WITH GRANT OPTION;