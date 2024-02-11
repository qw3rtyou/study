---
sticker: lucide//file
---
- 아파치의 기본 구조와 모듈
- 아파치의 주요 설정 파일, .htaccess 파일의 사용법
- Mysql 기본적인 SQL 쿼리문 작성 방법
- Mysql 데이터 조작 및 사용자 관리
- PHP 기본 문법과 변수
- PHP 함수의 정의와 사용
- PHP 폼 데이터 처리, 데이터베이스와의 연동


---
**1. 아파치 웹 서버의 대한 설명으로 올바른 것을 고르시오오**

- [x]  아파치는 모듈식 구조로, 추가 기능을 위해 다양한 모듈을 쉽게 설치하거나 제거할 수 있다.
- [ ]  아파치의 모든 설정은 `httpd.conf` 파일 하나에만 작성될 수 있다.
- [ ]  리눅스에서 아파치 설정 파일의 경로는 반드시 `/etc/apache2/apache2.conf` 이다.
- [ ]  아파치는 하나의 주 모듈만을 로드할 수 있으며, 다중 모듈 시스템을 지원하지 않는다.

**답 : 1**

1. 아파치는 모듈식 아키텍처를 가지고 있어, 필요에 따라 다양한 기능의 모듈을 추가하거나 제거할 수 있습니다.
2. 아파치의 설정은 `httpd.conf`를 포함해 여러 추가적인 설정 파일들에서 할 수 있으며, 사이트별로 별도의 설정 파일을 가질 수도 있습니다. 
3. 아파치 웹 서버의 설정 파일 경로는 시스템 구성에 따라 다를 수 있습니다. 일반적으로 리눅스 시스템에서 아파치 웹 서버의 설정 파일은 `/etc/apache2/apache2.conf` 경로에 위치할 수 있습니다. 그러나 이는 모든 리눅스 시스템에서 일반적으로 적용되는 것은 아닙니다.
4. 아파치는 다중 모듈을 로드하여 사용할 수 있으며, 이를 통해 서버의 기능을 확장할 수 있습니다.

---

**2. 아파치의 주요 설정 파일과 `.htaccess` 파일의 사용법에 대한 설명으로 맞는 것을 고르시오**

- [x]  `.htaccess` 파일은 디렉토리별로 서버 설정을 오버라이드할 수 있게 한다.
- [ ]  `.htaccess` 파일은 아파치 서버의 전역 설정을 변경하는 데 사용된다.
- [x]  `AllowOverride` 지시어를 통해 `.htaccess` 파일의 오**

- [x]  `SELECT * FROM users;` 쿼리는 `users` 테이블의 모든 레코드를 검색한다.
- [ ]  `UPDATE users SET name = 'nogon' WHERE id = 1;` 쿼리는 모든 사용자의 이름을 `nogon`으로 변경한다.
- [x]  `INSERT INTO users (name, email) VALUES ('nogon', 'nogon@example오**

- [x]  `GRANT ALL PRIVILEGES ON database.* TO 'user'@'localhost';`는 특정 사용자에게 모든 권한을 부여한다.
- [ ]  `REVOKE INSERT ON database.* FROM 'user'@'localhost';` 쿼리는 사용자에게 데이터 삽입 권한을 부여한다.
- [x]  `CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';`는 새로운 사용자를 생성한다.
- [ ]  사용자가 데이터베이스에 접근할 수 있게 하려면 반드시 `GRANT` 문을 사용해야만 한다.

**답 : 1, 3**

1. `GRANT ALL PRIVILEGES ON database.* TO 'user'@'localhost';` 명령은 `user` 사용자에게 `database` 데이터베이스의 모든 테이블에 대한 모든 권한을 부여합니다.
2. `REVOKE INSERT ON database.* FROM 'user'@'localhost';` 명령은 `user` 사용자의 데이터 삽입 권한을 취소합니다.
3. `CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';` 명령은 `newuser`라는 이름과 `password`라는 비밀번호를 가진 새로운 사용자를 생성합니다.
4. 사용자가 데이터베이스에 접근할 수 있는 다양한 방법이 있을 수 있으며, `GRANT` 명령은 권한을 부여하는 한 가지 방법일 뿐입니다.

---

**5. 다음 PHP 코드에 대한 설명으로 올바른 것을 고르시오**
```php
<?php
$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "myDB";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "INSERT INTO user (firstname, lastname, email)
VALUES ('no', 'gon', 'nogon@example.com')";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>
```

- [x]   `mysqli` 클래스를 사용하여 MySQL 데이터베이스에 연결하였다.
- [x]   DB 연결에 실패하면 연결 에러 메시지를 출력하고 프로그램을 즉시 종료한다.
- [ ]   `$conn->query($sql) === TRUE` 조건비교는 일반적으로 `==`를 사용하므로 `===` 대신 `==`로 수정해야 한다.
- [ ]   위의 코드는 MySQL 쿼리 실행 성공 여부와는 독립적으로 동작한다.

**답 : 1, 2**

1. `mysqli` 클래스를 사용하여 MySQL 데이터베이스에 연결합니다.
2. 연결에 실패하면 연결 에러 메시지를 출력하고 프로그램을 종료합니다.
3. `$conn->query($sql) === TRUE` 조건비교는 PHP에서 `===`는 값을 비교하는 것뿐만 아니라 데이터 타입까지 체크합니다. 따라서 이를 `==`로 수정하는 것은 권장하지 않습니다.
4. 위의 코드는 MySQL 쿼리 실행 성공 여부에 따라 다른 메시지를 출력하므로, MySQL 쿼리 실행과 독립적으로 동작하지 않습니다.

---

**6. 다음 PHP 코드에 대한 설명으로 올바른 것을 모두 고르시오**
```php
<?php
$fp = fsockopen("www.example.com", 80, $errno, $errstr, 30);
if (!$fp) {
    echo "$errstr ($errno)<br />\n";
} else {
    $out = "GET / HTTP/1.1\r\n";
    $out .= "Host: www.example.com\r\n";
    $out .= "Connection: Close\r\n\r\n";
    fwrite($fp, $out);
    while (!feof($fp)) {
        echo fgets($fp, 128);
    }
    fclose($fp);
}
?>
```

- [ ]  `fsockopen`함수에서 마지막 인자 30은 타임아웃 시간이다.
- [x]  연결에 실패하면 에러 번호와 에러 메시지를 출력한다.
- [ ]  연결 성공 후, HTTP POST 요청을 보내고 응답을 출력한다.
- [ ]  PHP에서 자동으로 소켓 연결을 종료하게 된다.

**답 : 1, 2**

1. `fsockopen` 함수에서 30은 타임아웃 시간입니다. 참고로 2번째 인자 80은 포트번호입니다.
2. 연결에 실패하면 에러 번호와 에러 메시지를 출력합니다.
3. 연결 성공 후, POST가 아닌 GET 요청을 보내고 응답을 출력합니다.
4. `fclose` 함수를 사용하여 소켓 연결을 종료합니다. PHP는 자동으로 소켓을 종료할 수 없습니다.
---

**7. 다음 PHP 코드에 대한 설명으로 올바른 것을 고르시오
```php
<?php
$x = 5;
function test() {
    global $x;
    $x += 5;
    $y = 10;
    echo $x;
}
test();
echo $x;
echo $y;
?>
```

- [x]  `test` 함수 내에서 `global` 키워드를 사용하여 전역 변수 `$x`에 접근하였다.
- [x]  `test` 함수 내에서 전역 변수 `$x`의 값이 5 증가한 후 출력되었다.
- [ ]  `test` 함수 외부에서 `$x`의 값은 변하지 않았다.
- [ ]  `test` 함수 외부에서 `$y`의 값이 출력되었다.

**답 : 1, 2**

1. `test` 함수 내부에서 `global` 키워드를 사용하여 전역 변수 `$x`에 접근하였습니다. 이를 통해 함수 내부에서도 `$x`의 값을 변경할 수 있습니다.
2. `test` 함수 내부에서 `$x`의 값에 5를 더한 후 출력하였습니다. 따라서 이 경우, `$x`의 값은 10이 되고, 이 값이 출력됩니다.
3. `test` 함수 외부에서 `$x`의 값을 출력하면, 함수 내부에서 변경된 값인 10이 출력됩니다. `test` 함수 내부에서 `global` 키워드를 사용하여 전역 변수 `$x`에 접근하였기 때문에 `$x`의 값이 변경됩니다.
4. `$y`는 `test` 함수 내부에서 선언된 지역 변수입니다. 따라서 함수 외부에서는 `$y`의 값을 출력할 수 없으며, 이 경우 에러가 발생합니다.

 