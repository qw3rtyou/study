
# PHP: Hypertext Preprocessor

<aside> 💡 이번에 공부할 내용은 다음과 같습니다.

1. PHP의 개념과 특징
2. PHP 기본 문법과 변수
3. 함수의 정의와 사용
4. 폼 데이터 처리
5. 데이터베이스와의 연동

PHP는 서버 측에서 실행되는 스크립트 언어로, 동적인 웹 페이지를 생성하기 위해 널리 사용됩니다. HTML 코드 내에 PHP 코드를 삽입할 수 있으며, 데이터베이스와의 상호작용을 쉽게 처리할 수 있습니다.

</aside>

---

- PHP의 기본 문법과 변수 사용
```php
<?php
$name = "World";
echo "Hello, $name!";

if ($name == "World") {
    echo "The name is World.";
} else {
    echo "The name is not World.";
}

for ($i = 0; $i < 5; $i++) {
    echo "The number is $i <br />";
}
?>
```

- 함수의 정의와 사용
```php
<?php
function add($num1, $num2) {
    return $num1 + $num2;
}

$result = add(5, 10);
echo "The result is $result"; 
?>
```

- 폼 데이터 처리
```php
<!-- HTML에서 폼을 정의 -->
<form method="post" action="process.php">
    Name: <input type="text" name="name" />
    <input type="submit" />
</form>

<?php
$name = $_POST['name'];
echo "Hello, $name!";
?>
```

- 데이터베이스와의 연동
```php
<?php
$conn = new mysqli("localhost", "username", "password", "database");

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT id, name FROM users";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        echo "id: " . $row["id"]. " - Name: " . $row["name"]. "<br />";
    }
} else {
    echo "0 results";
}
$conn->close();
?>
```

---

<aside> 🔥 다음과 같은 내용에 도전해봅시다.

1. php 설치 후 실습해보기
2. GET과 POST의 차이점 이해하기
3. 파일 업로드 방법 이해하기

</aside>