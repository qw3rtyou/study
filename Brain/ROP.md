[[RTL]]

Return Oriented Programming
# 배경
RTL에서 다수의 리턴 가젯을 연결해서 사용하여 복잡한 실행 흐름을 구현하는 기법
ASLR이 걸린 환경에서 `system` 함수를 사용하려면 프로세스에서 libc가 매핑된 주소를 찾고, 그 주소로부터 `system` 함수의 오프셋을 이용하여 함수의 주소를 계산해야 함
ROP는 이런 복잡한 제약 사항을 유연하게 해결할 수 있는 수단을 제공
ROP 페이로드는 리턴 가젯으로 구성되는데, `ret` 단위로 여러 코드가 연쇄적으로 실행되는 모습에서 ROP chain이라고도 불림


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