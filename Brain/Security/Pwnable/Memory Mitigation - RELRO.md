
RELocation Read-Only

# 배경
Lazy binding을 하는 바이너리는 실행 중에 GOT 테이블을 업데이트할 수 있어야 하므로 GOT에 쓰기 권한이 부여됨
이는 바이너리를 취약하게 만드는 원인이 될 수 있음
RELRO는 쓰기 권한이 불필요한 데이터 세그먼트에 쓰기 권한을 제거
RELRO는 RELRO를 적용하는 범위에 따라 두 가지로 구분
하나는 RELRO를 부분적으로 적용하는 Partial RELRO이고, 나머지는 가장 넓은 영역에 RELRO를 적용하는 Full RELRO임

- Partail RELRO
Partail RELRO는 `.init_array`와 `.fini_array`에 대한 쓰기 권한이 제거되어 두 영역을 덮어쓰는 공격을 수행하기 어려워지지만, `.got.plt` 영역에 대한 쓰기 권한이 존재하므로 **GOT overwrite** 공격을 활용할 수 있음

- Full RELRO
Full RELRO는 `.init_array`, `.fini_array` 뿐만 아니라 `.got` 영역에도 쓰기 권한이 제거됨 -> GOT Overwrite 불가능

#  섹션 분석
자신의 메모리 맵을 출력하는 바이너리 소스 코드
```c
// Name: relro.c
// Compile: gcc -o prelro relro.c -no-pie -fno-PIE
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
int main() {
  FILE *fp;
  char ch;
  fp = fopen("/proc/self/maps", "r");
  while (1) {
    ch = fgetc(fp);
    if (ch == EOF) break;
    putchar(ch);
  }
  return 0;
}
```

내가 분석하고 싶은 주소가 어떤 권한을 가지는지, 어떤 코드에서 온 것인지 한눈에 알 수 있음(nmap 사용하면 됨)
```sh
$ ./prelro
00400000-00401000 r--p 00000000 08:02 2886150                            /home/dreamhack/prelro
00401000-00402000 r-xp 00001000 08:02 2886150                            /home/dreamhack/prelro
00402000-00403000 r--p 00002000 08:02 2886150                            /home/dreamhack/prelro
00403000-00404000 r--p 00002000 08:02 2886150                            /home/dreamhack/prelro
00404000-00405000 rw-p 00003000 08:02 2886150                            /home/dreamhack/prelro
0130d000-0132e000 rw-p 00000000 00:00 0                                  [heap]
7f108632c000-7f108632f000 rw-p 00000000 00:00 0
7f108632f000-7f1086357000 r--p 00000000 08:02 132492                     /usr/lib/x86_64-linux-gnu/libc.so.6
7f1086357000-7f10864ec000 r-xp 00028000 08:02 132492                     /usr/lib/x86_64-linux-gnu/libc.so.6
7f10864ec000-7f1086544000 r--p 001bd000 08:02 132492                     /usr/lib/x86_64-linux-gnu/libc.so.6
7f1086544000-7f1086548000 r--p 00214000 08:02 132492                     /usr/lib/x86_64-linux-gnu/libc.so.6
7f1086548000-7f108654a000 rw-p 00218000 08:02 132492                     /usr/lib/x86_64-linux-gnu/libc.so.6
7f108654a000-7f1086557000 rw-p 00000000 00:00 0
7f1086568000-7f108656a000 rw-p 00000000 00:00 0
7f108656a000-7f108656c000 r--p 00000000 08:02 132486                     /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
7f108656c000-7f1086596000 r-xp 00002000 08:02 132486                     /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
7f1086596000-7f10865a1000 r--p 0002c000 08:02 132486                     /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
7f10865a2000-7f10865a4000 r--p 00037000 08:02 132486                     /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
7f10865a4000-7f10865a6000 rw-p 00039000 08:02 132486                     /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
7ffe55580000-7ffe555a1000 rw-p 00000000 00:00 0                          [stack]
7ffe555de000-7ffe555e2000 r--p 00000000 00:00 0                          [vvar]
7ffe555e2000-7ffe555e4000 r-xp 00000000 00:00 0                          [vdso]
ffffffffff600000-ffffffffff601000 --xp 00000000 00:00 0 
```


# Hook Overwrite
[[Hook Overwrite]]