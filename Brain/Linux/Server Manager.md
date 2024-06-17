# 로깅
### 특정 사용자의 로그인 시도
```
grep 'username' /var/log/auth.log	#특정 사용자의 로그인 시도
grep 'Failed' /var/log/auth.log	#실패한 로그인 시도
grep '192.168.1.1' /var/log/auth.log	#특정 IP로 부터 로그인 시도
```