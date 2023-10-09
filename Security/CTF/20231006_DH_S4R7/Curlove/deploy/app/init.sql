CREATE DATABASE test_db CHARACTER SET utf8;
CREATE USER 'curlove_user'@'localhost' IDENTIFIED BY 'curlove_password';
GRANT ALL PRIVILEGES ON test_db.* TO 'curlove_user'@'localhost';

USE `test_db`;
CREATE TABLE users (
  idx int auto_increment primary key,
  username varchar(128) not null,
  password varchar(128) not null
);

INSERT INTO users (username, password) values ('admin1', '22d053d7324aa0572dbeeacd4d4614293153ef7dbe6b2eddda05bf300765973d');
INSERT INTO users (username, password) values ('admin2', '42ebd7d81cf75344e2102ab720aecad786d5d25af051df0feb160f1cc78a525e');
INSERT INTO users (username, password) values ('admin3', '6f2854dbd635e45e5d51c0139aec7ee6ec605b56288b1e41412172d584da856c');
INSERT INTO users (username, password) values ('admin4', 'ebffbacb422e19b3265084a9c926e999f14172729cf44d86a7977be5f6a7fd1b');
