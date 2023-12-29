Local File Inclusion
공격자가 웹 애플리케이션의 다른 파일들을 읽어오거나, 때로는 외부 파일들까지 포함시키는 공격


# 공격경로
- 웹 애플리케이션의 로컬 파일 읽기
?p=../path/to/file

- 로깅 파일 읽기
/var/log/apache2/access.log

- 세션 파일 읽기
/var/lib/php/sessions/

# PHP Wrappper
PHP는 여러 가지 스트림 래퍼(stream wrapper)를 제공하며, 이를 이용하면 LFI 공격을 확장할 수 있음
- `php://filter`
파일의 내용을 base64로 인코딩 할 수 있음

`?p=php://filter/read=convert.base64-encode/resource=lfiflag.php`

- `php://input`
POST 요청으로 전송된 원시 데이터를 읽을 수 있음
이 스트림은 읽기 전용이며, `$_POST`나 `$_FILES`와는 달리 PHP 처리가 적용되지 않은 원시 데이터를 제공

- `php://output`
출력 스트림으로, 일반적으로는 `echo`나 `print`와 같은 함수로 데이터를 출력할 때 사용

