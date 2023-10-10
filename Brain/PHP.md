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