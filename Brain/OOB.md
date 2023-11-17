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

# 예시1

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

먼저, 초기화하기 전에 배열의 요소들을 출력할 수 있는데,
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
GDB로 분석해보면, `0xfff6dd40`에서 메인의 스택프레임이 끝나지만 그 뒤로도 사용되고 버려진 데이터들이 꽤 많다는 걸 확인 할 수 있음

```sh
pwndbg> x/100x $esp-0x30
0xfff6dd10:	0xf7e2a620	0x5659005b	0xfff6dd34	0x00000002
0xfff6dd20:	0x56590053	0x56591fb4	0xf7c58c69	0x5658f3ce
0xfff6dd30:	0x5659005b	0xfff6dd44	0xfff6de08	0x5658f3b8
0xfff6dd40:	0xf7fccba0	0x00000005	0x00000009	0x0000000a
0xfff6dd50:	0x0000000b	0x0000000c	0x0000000d	0x0000000f
0xfff6dd60:	0x00000012	0x00000014	0x0000001a	0x0000001c
0xfff6dd70:	0x00000023	0x0000002e	0x00000036	0x0000003f
0xfff6dd80:	0x00000042	0x00000046	0x00000046	0x0000004f
0xfff6dd90:	0x00000054	0x00000054	0x00000000	0xf7fcc000
0xfff6dda0:	0xf7f93540	0xffffffff	0x5658e034	0xf7f956d0
0xfff6ddb0:	0xf7fcc608	0x0000000b	0xfff6de1c	0xfff6dfcc
0xfff6ddc0:	0x00000000	0x00000000	0x01000000	0x0000000b
0xfff6ddd0:	0xf7f93540	0x00000000	0xf7c184be	0xf7e2a054
0xfff6dde0:	0xf7f8d4a0	0xf7fa5f90	0xf7c184be	0xf7f8d4a0
0xfff6ddf0:	0xfff6de30	0xf7f8d66c	0xf7f8db30	0x00000014
0xfff6de00:	0xfff6de20	0xf7e2a000	0xf7fcc020	0xf7c21519
0xfff6de10:	0xfff6e30e	0x00000070	0xf7fcc000	0xf7c21519
0xfff6de20:	0x00000001	0xfff6ded4	0xfff6dedc	0xfff6de40
0xfff6de30:	0xf7e2a000	0x5658f34c	0x00000001	0xfff6ded4
0xfff6de40:	0xf7e2a000	0xfff6ded4	0xf7fcbb80	0xf7fcc020
0xfff6de50:	0x8097f83a	0xe902122a	0x00000000	0x00000000
0xfff6de60:	0x00000000	0xf7fcbb80	0xf7fcc020	0x9b8e2200
0xfff6de70:	0xf7fcca40	0xf7c214a6	0xf7e2a000	0xf7c215f3
0xfff6de80:	0x00000000	0x56591eb8	0xfff6dedc	0xf7fcc020
0xfff6de90:	0x00000000	0x00000000	0xf7c2156d	0x56591fb4
```

---

이 중에서 `0x5658f3b8`를 살펴보면, 실제 명령어를 확인해보니 main의 실제 주소 값이 들어 있음을 알 수 있음

```sh
pwndbg> x/i 0x5658f3b8
   0x5658f3b8 <main+108>:	sub    esp,0x8
```

같은 방법으로 잘 찾아보면 scanf의 위치같이 라이브러리의 주소의 대략적인 위치도 알 수 있게 됨

```sh
pwndbg> x/i 0x5659005b
   0x5659005b:	and    eax,0x72610064
pwndbg> x/i 0xf7e2a620
   0xf7e2a620 <_IO_2_1_stdin_>:	mov    esp,DWORD PTR [eax]
pwndbg> x/i 0xfff6dd34
   0xfff6dd34:	inc    esp
pwndbg> x/i 0xf7c58c69
   0xf7c58c69 <__isoc99_scanf+9>:	add    eax,0x1d1397
pwndbg>
```

---

이렇게 런타임 중에 메모리에 적재된 데이터들의 위치를 확인하여 5번 매뉴에서 SBO를 할 수 있게 됨

```sh
0x0000148f <+323>:	cmp    eax,0x4
0x00001492 <+326>:	jne    0x1518 <main+460>
0x00001498 <+332>:	sub    esp,0xc
0x0000149b <+335>:	lea    eax,[ebx-0x1f48]
0x000014a1 <+341>:	push   eax
0x000014a2 <+342>:	call   0x1080 <puts@plt>
0x000014a7 <+347>:	add    esp,0x10
0x000014aa <+350>:	sub    esp,0x8
0x000014ad <+353>:	lea    eax,[ebp-0xc4]
0x000014b3 <+359>:	push   eax
0x000014b4 <+360>:	lea    eax,[ebx-0x1f59]
0x000014ba <+366>:	push   eax
0x000014bb <+367>:	call   0x10c0 <__isoc99_scanf@plt>
0x000014c0 <+372>:	add    esp,0x10
0x000014c3 <+375>:	mov    eax,DWORD PTR [ebp-0xc4]
0x000014c9 <+381>:	cmp    eax,0x13
0x000014cc <+384>:	jg     0x14f7 <main+427>
0x000014ce <+386>:	mov    eax,DWORD PTR [ebp-0xc4]
0x000014d4 <+392>:	mov    edx,DWORD PTR [ebp+eax*4-0xc0]
0x000014db <+399>:	mov    eax,DWORD PTR [ebp-0xc4]
0x000014e1 <+405>:	sub    esp,0x4
0x000014e4 <+408>:	push   edx
0x000014e5 <+409>:	push   eax
0x000014e6 <+410>:	lea    eax,[ebx-0x1f56]
0x000014ec <+416>:	push   eax
0x000014ed <+417>:	call   0x1060 <printf@plt>
0x000014f2 <+422>:	add    esp,0x10
0x000014f5 <+425>:	jmp    0x1509 <main+445>
0x000014f7 <+427>:	sub    esp,0xc
0x000014fa <+430>:	lea    eax,[ebx-0x1f27]
0x00001500 <+436>:	push   eax
0x00001501 <+437>:	call   0x1080 <puts@plt>
0x00001506 <+442>:	add    esp,0x10
0x00001509 <+445>:	mov    DWORD PTR [ebp-0xc4],0x4
0x00001513 <+455>:	jmp    0x13b3 <main+103>
```
