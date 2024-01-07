# MySQL 데이터베이스

<aside> 💡 이번에 공부할 내용은 다음과 같습니다.

1. MySQL의 개념과 특징
2. 데이터베이스 및 테이블 생성 방법
3. 기본적인 SQL 쿼리문 작성 방법
4. 데이터 조작 및 관리

MySQL은 관계형 데이터베이스 관리 시스템(RDBMS)으로, 데이터를 효율적으로 저장, 관리 및 검색을 위해 SQL(Structured Query Language)을 사용합니다. 오픈 소스이며, 다양한 운영 체제에서 사용할 수 있습니다.

</aside>

---

- MySQL의 기본 구조와 데이터베이스 생성 예시
```sql

CREATE DATABASE example;

USE example;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL
);
```

- 데이터 조작 및 관리를 위한 기본적인 SQL 쿼리문

```sql
INSERT INTO users (username, email) VALUES ('user1', 'user1@example.com');
SELECT * FROM users;
UPDATE users SET email = 'newemail@example.com' WHERE id = 1;
DELETE FROM users WHERE id = 1;
```

- 데이터베이스 관리
```sql
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON example_db.* TO 'newuser'@'localhost';
```

```sh
mysqldump -u username -p example_db > example_db_backup.sql
mysql -u username -p example_db < example_db_backup.sql
```

---

<aside> 🔥 다음과 같은 내용에 도전해봅시다.

1. Mysql 로컬 환경에서 설치 후 위의 내용 실습하기
2. JOIN을 사용하여 여러 테이블 간 관계 설정하기 

</aside>