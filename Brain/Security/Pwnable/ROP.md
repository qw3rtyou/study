[[RTL]]

Return Oriented Programming
# 배경
RTL에서 다수의 리턴 가젯을 연결해서 사용하여 복잡한 실행 흐름을 구현하는 기법
ASLR이 걸린 환경에서 `system` 함수를 사용하려면 프로세스에서 libc가 매핑된 주소를 찾고, 그 주소로부터 `system` 함수의 오프셋을 이용하여 함수의 주소를 계산해야 함
ROP는 이런 복잡한 제약 사항을 유연하게 해결할 수 있는 수단을 제공
ROP 페이로드는 리턴 가젯으로 구성되는데, `ret` 단위로 여러 코드가 연쇄적으로 실행되는 모습에서 ROP chain이라고도 불림


# x86, x64 페이로드 차이점
x86 payload
```python
# write(1,read_got,4)
payload+=p32(write_plt)
payload+=p32(pop3gdgt)
payload+=p32(1)
payload+=p32(read_got)
payload+=p32(4)
```

x64 payload
```python
# write(1, read_got, ...)
payload+=p64(pop_rdi)
payload+=p64(1)
payload+=p64(pop_rsi_r15)
payload+=p64(read_got)
payload+=p64(0)
payload+=p64(write_plt)
```

페이로드 순서가 다른 이유는 두 아키텍처가 함수 인자를 전달하는 방식의 차이 때문
x86 아키텍처에서는 함수의 인자가 주로 스택을 통해 전달되지만
x64 아키텍처에서는 함수의 인자가 주로 레지스터를 통해 전달하기 때문에
x86에서는 먼저 함수를 사용하면서 스택에 있는 인자들을 사용한 다음 나중에 가젯을 통해 스택을 정리한 반면,
x64에서는 먼저 인자를 설정한 다음, write의 파라미터로 사용함



# ELF header로 라이브러리 속 함수 위치 찾기
```sh
┌──(foo1㉿main-server)-[~/Desktop/dh/rop]
└─$ readelf -s /lib/x86_64-linux-gnu/libc.so.6 |grep " read@"
   289: 00000000001149c0   157 FUNC    GLOBAL DEFAULT   15 read@@GLIBC_2.2.5

┌──(foo1㉿main-server)-[~/Desktop/dh/rop]
└─$ readelf -s /lib/x86_64-linux-gnu/libc.so.6 |grep " system@"
  1481: 0000000000050d70    45 FUNC    WEAK   DEFAULT   15 system@@GLIBC_2.2.5
```

```sh
┌──(foo1㉿main-server)-[~/Desktop/dh/rop]
└─$ readelf -s libc.so.6 |grep " read@"
   289: 0000000000114980   157 FUNC    GLOBAL DEFAULT   15 read@@GLIBC_2.2.5

┌──(foo1㉿main-server)-[~/Desktop/dh/rop]
└─$ readelf -s libc.so.6 |grep " system@"
  1481: 0000000000050d60    45 FUNC    WEAK   DEFAULT   15 system@@GLIBC_2.2.5
```


# 예제1
[[Dreamhack - rop]]

# 예제2
[[Dreamhack - basic_rop_x86]]

