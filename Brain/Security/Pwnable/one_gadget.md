**원 가젯(one-gadget)** 또는 **magic_gadget**
실행하면 셸이 획득되는 코드 뭉치

# 설치
```sh
sudo apt-get install ruby-full
sudo gem install one_gadget
```

# 배경
기존에는 셸을 획득하기 위해 여러 개의 가젯을 조합해서 ROP Chain을 구성하거나 RTL 공격을 수행했지만, 원 가젯은 단일 가젯만으로도 셸을 실행할 수 있는 매우 강력한 가젯임

원 가젯은 libc의 버전마다 다르게 존재하며, 제약 조건도 모두 다름
일반적으로 Glibc 버전이 높아질수록 제약 조건을 만족하기가 어려워지는 특성이 있기 때문에 필요에 따라 상황에 맞는 가젯을 사용하거나, 제약 조건을 만족하도록 사전에 조작해 주어야 함

원 가젯은 함수에 인자를 전달하기 어려울 때 유용하게 활용할 수 있음
예를 들어, 훅오버라이트 문제를 풀 때, `__malloc_hook` 을 임의의 값으로 오버라이트할 수 있지만, `malloc` 의 인자에 작은 정수 밖에 입력할 수 없는 상황이라면 `“/bin/sh”` 문자열 주소를 인자로 전달하기가 매우 어려울 수 있음
이럴 때 제약 조건을 만족하는 원 가젯이 존재한다면, 이를 호출해서 셸을 획득할 수 있음


# 사용법
`one_gadget [탐색대상.so]`
`/bin/sh`이라는 문자열이 있는 `glibc`에서 실행해야 함
```sh
┌──(foo1㉿main-server)-[~/Desktop/Dreamhack/fho]
└─$ one_gadget libc-2.27.so 
0x4f3d5 execve("/bin/sh", rsp+0x40, environ)
constraints:
  rsp & 0xf == 0
  rcx == NULL

0x4f432 execve("/bin/sh", rsp+0x40, environ)
constraints:
  [rsp+0x40] == NULL

0x10a41c execve("/bin/sh", rsp+0x70, environ)
constraints:
  [rsp+0x70] == NULL

┌──(foo1㉿main-server)-[~/Desktop/Dreamhack/fho]
└─$ one_gadget /lib/x86_64-linux-gnu/libc.so.6
0x50a47 posix_spawn(rsp+0x1c, "/bin/sh", 0, rbp, rsp+0x60, environ)
constraints:
  rsp & 0xf == 0
  rcx == NULL
  rbp == NULL || (u16)[rbp] == NULL

0xebc81 execve("/bin/sh", r10, [rbp-0x70])
constraints:
  address rbp-0x78 is writable
  [r10] == NULL || r10 == NULL
  [[rbp-0x70]] == NULL || [rbp-0x70] == NULL

0xebc85 execve("/bin/sh", r10, rdx)
constraints:
  address rbp-0x78 is writable
  [r10] == NULL || r10 == NULL
  [rdx] == NULL || rdx == NULL

0xebc88 execve("/bin/sh", rsi, rdx)
constraints:
  address rbp-0x78 is writable
  [rsi] == NULL || rsi == NULL
  [rdx] == NULL || rdx == NULL

```