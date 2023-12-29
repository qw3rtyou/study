Address Space Layout Randomization

# 배경
바이너리가 실행될 때마다 주요 데이터 영역(스택, 힙, 공유 라이브러리)을 임의의 주소에 할당하는 보호 기법

```c
// Name: addr.c
// Compile: gcc addr.c -o addr -ldl -no-pie -fno-PIE

#include <dlfcn.h>
#include <stdio.h>
#include <stdlib.h>

int main() {
  char buf_stack[0x10];                   // 스택 버퍼
  char *buf_heap = (char *)malloc(0x10);  // 힙 버퍼

  printf("buf_stack addr: %p\n", buf_stack);
  printf("buf_heap addr: %p\n", buf_heap);
  printf("libc_base addr: %p\n",
         *(void **)dlopen("libc.so.6", RTLD_LAZY));  // 라이브러리 주소

  printf("printf addr: %p\n",
         dlsym(dlopen("libc.so.6", RTLD_LAZY),
               "printf"));  // 라이브러리 함수의 주소
  printf("main addr: %p\n", main);  // 코드 영역의 함수 주소
}
```

```sh
$ gcc addr.c -o addr -ldl -no-pie -fno-PIE

$ ./addr
buf_stack addr: 0x7ffcd3fcffc0
buf_heap addr: 0xb97260
libc_base addr: 0x7fd7504cd000
printf addr: 0x7fd750531f00
main addr: 0x400667
$ ./addr
buf_stack addr: 0x7ffe4c661f90
buf_heap addr: 0x176d260
libc_base addr: 0x7ffad9e1b000
printf addr: 0x7ffad9e7ff00
main addr: 0x400667
$ ./addr
buf_stack addr: 0x7ffcf2386d80
buf_heap addr: 0x840260
libc_base addr: 0x7fed2664b000
printf addr: 0x7fed266aff00
main addr: 0x400667
```

- main 함수를 제외한 모든 주소는 실행할 때 변경됨
- 바이너리를 반복해서 실행해도 `libc_base` 주소 하위 12비트 값과 `printf` 주소 하위 12비트 값은 변경되지 않음
리눅스는 ASLR이 적용됐을 때, 파일을 페이지(page) 단위로 임의 주소에 매핑함
따라서 페이지의 크기인 12비트 이하로는 주소가 변경되지 않음
- libc_base와 `printf`의 주소 차이는 항상 같음  
ASLR이 적용되면, 라이브러리는 임의 주소에 매핑
그러나 라이브러리 파일을 그대로 매핑하는 것이므로 매핑된 주소로부터 라이브러리의 다른 심볼들 까지의 거리(Offset)는 항상 같음



# 커널의 ASLR 사용 확인  
`$ cat /proc/sys/kernel/randomize_va_space`
- No ASLR(0): ASLR을 적용하지 않음
- Conservative Randomization(1): 스택, 힙, 라이브러리, vdso 등
- Conservative Randomization + brk(2): (1)의 영역과 `brk`로 할당한 영역