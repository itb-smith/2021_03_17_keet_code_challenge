USE keet;

CREATE TABLE users (
    id VARCHAR(13) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    gender char(1) NOT NULL,
    visit_date DATE NOT NULL,
    PRIMARY KEY (id)
);

LOAD DATA INFILE 'users.csv' 
INTO TABLE USERS 
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

CREATE TABLE daily_user_counts (
    `year` BIGINT NOT NULL,
    `month` BIGINT NOT NULL,
    `day` BIGINT NOT NULL,
    observed BIGINT NULL,
    counts BIGINT NULL,
    PRIMARY KEY (`year`, `month`, `day`)
);