
# 출처
http://sosal.tistory.com/

# GDB
GDB는 컴퓨터 프로그램을 실행하여, 사용자에게 실행 과정을 추적하고,
중간에 임의로 수정, 심볼(함수,변수)들을 모니터링을 할 수 있도록 함


# GDB 설치
0. GDB
```sh
sudo apt-get install gdb
```

1. PEDA
Python Exploit Development Assistance for GDB
```sh
git clone https://github.com/longld/peda.git ~/peda
echo "source ~/peda/peda.py" >> ~/.gdbinit
echo "DONE! Please restart your GDB."
```

2. pwndbg
```sh
git clone https://github.com/pwndbg/pwndbg
cd pwndbg
./setup.sh
```

3. GEF
GDB Enhanced Features
```sh
git clone https://github.com/hugsy/gef.git
echo source $(realpath gef.py) >> ~/.gdbinit
```


# 디버깅 정보를 담아 컴파일 하기

	gcc -g source.c -o program
	gcc -g -o program source.c

디버그 모드로 컴파일된 program과 옵션 없이 컴파일된 program1 의 size를 보면
디버그 모드로 된 program 의 크기가 더욱 큰 것을 볼 수 있다. (디버깅 정보가 삽입)
디버깅 정보에는 프로그램에서 사용하는 심볼정보 (변수, 함수, 문자열, 각각의 주소 등)와
컴파일에 사용된 소스, 그리고 컴파일된 인스트럭션들이 어떤 소스의 행에 해당하는 정보 등이 포함된다.
이 정보들을 이용하여 프로그램의 어셈블리 코드와 C언어를 동시에 보면서 디버깅 하는 것이 가능하다.

# gdb 실행하기, 프로그램 디버깅 시작하기, gdb 종료하기

### gdb 실행하기
```bash
gdb [프로그램명]                      //일반 파일 디버깅
gdb [프로그램명] [프로세스 PID] //프로세스 디버깅
(gdb) run  argv[1] argv[2]...  // (또는 r argv[1].... )
```

gdb 상에서 프로그램이 실행

프로그램이 지원하는 새로운 권한 (setuid 등)은 상속되지 않음

실행 후 중간에 멈춘 후, 다시 run 명령을 했을 경우
프로그램을 새로 처음부터 시작

# 프로그램의 c언어 소스 보기 (디버깅 정보 포함)

	l (또는 list) :: 프로그램 소스의 정보가 출력된다. (-g 디버깅정보가 포함되어있어야 가능)
	   default로 10줄의 소스를 보여준다.
	   다시 l을 누르거나 Enter를 치면 다음 10줄의 소스를 보여준다.
   
	l [number] :: 입력된 수만큼의 소스를 출력한다.

	set listsize [number] 명령어를 통해 출력되는 행의 갯수를 조절할 수 있다.

	l [function] 지정된 함수의 소스를 출력한다.
	<여러개의 파일로 컴파일 된 경우>
	l [file.c]:[number] 
	l [file.c]:[function]

# 프로그램의 어셈블리 코드 보기

	disassemble (disas, disass, disasse.... ):: 프로그램의 어셈블리 코드 보기

	disas [function] :: 함수 부분의 disassemble 한 코드들을 보여준다.

	disas main

	disas [0xffffffa0] [0xffffffffa9] :: 주소 범위 사이의 어셈블리 코드를 보인다.

# break 포인트. 디버깅 실행과 진행어

run (or r) 명령어로 실행 시키면
프로그램이 처음부터 끝날 때까지 실행되기만 한다.
이래서는 중간 중간의 심볼 현황을 살펴 볼 수 없다.
그래서 원하는 순간에 멈추기 위해 break (b) 명령어를 사용한다.

	break (b) :: run 명령어가 실행된 후 멈출 메모리 위치

	b [function]            // 함수 시작부분에 브레이크 포인트 설정
	b [number]            // 어셈블리 코드에서 10행에 브레이크 포인트 설정
	                // 아래는 프로그램의 소스가 여러 파일로 이루어졌을 경우
	b [file.c]:[function]
	b [file.c]:[number]
	cl 명령어로 브레이크 포인트를 지울 수 있다.
	d :: 모든 브레이크를 지운다.
	
브레이크 포인트를 건 다음, run 실행시키면 원하는 곳까지 진행한다.

`b *caller+50`

##### 프로그램 진행 루틴 다루기

	ni     :: 어셈블리 소스의 한줄을 실행한다. 함수가 호출되는 부분도 한줄로 인식한다.
	si     :: 어셈블리 소스의 한줄을 실행하는데, 함수가 호출된다면 함수루틴으로 들어간다.
	next (n) :: c언어 소스의 한줄을 실행한다. 함수 호출시, 한줄로 처리하여 함수를 수행한다.
	step (s) :: c언어 소스의 한줄을 실행한다. 함수 호출시, 함수 루틴 안으로 들어간다.
	(위 두 명령어는 디버깅 정보가 없다면 run이 된다.)
	(ni, si, n, s, 명령어 뒤에 숫자를 붙일 시 그 수만큼 진행한다. ex: ni 5 ,   s 5)
	c     : 브레이크 포인트를 만날 때 까지 계속 진행한다.
	finish  (f) : 함수가 끝난 지점으로 이동한다. (함수가 끝날 때 까지 모조리 실행)
	return (r) : 함수가 끝난 지점으로 이동한다. (현재 함수를 실행하지 않는다.)
	return 123 // 함수의 리턴값 123
	until   (u) : 현재 루프를 빠져나간다.
	kill (k) : 프로세스 종료

# 변수, 포인터 값 보기, 출력 형식 지정, 값 모니터링 하기

### 지역변수 / 전역변수 값 보기

	info locals :: 현재 eip가 가리키고 있는 위치의 지역변수를 모두 출력한다.
	info variables :: 현재상태에서의 전역변수 리스트를 확인할 수 있다.
	find /b &system, +999999999, "/bin/sh"
	grep /bin/sh
	
	p [value] :: (point의 약자) 변수 하나의 값을 보여줌
	변수 이름이 중복 될 때,
	p  'file name.c'::[value] // 전역변수
	p   [function]::[value]   // 지역변수(함수)
	출력 형식 지정
	p/[format] $보고자하는것
	p/t   //  2진수
	p/o  //  8진수
	p/d  // 10진수 (int)
	p/u  // 부호없는 10진수 (unsigned int)
	p/x  // 16진수 //주소를 보기위해 가장 많이 쓴다.
	p/c  // 문자형 출력 (크기가 4byte 이상인 변수는 처음 1바이트를 출력한다.)
	p/f   // 부동 소수점 값 형식으로 출력
	p/a  // 가장 가까운 심볼의 오프셋을 출력
		(p/a 0x0801295 를 입력하면, 0x0801295와 가장 가까운 어셈블리 명령어줄의 offset을 출력)
	void* buf = "hello world";
	(gdb) p (char *)buf // 형변환도 가능하다.

### 포인트 변수 값 보기

	p 명령어 (point) point 명령어는 변수 값, 함수의 주소값도 볼 수 있다.
	(gdb) info locals
	a = {_int = 10, _char = 37 '%', _double = -0.51}    //struct my_struct a
	b = (struct my_struct *) 0x251ff4                        //struct my_struct *b
	(gdb) p a                                              //구조체 a
	$1 = {_int = 10, _char = 37 '%', _double = -0.51}
	(gdb) p b
	$2 = (struct my_struct *) 0x251ff4                           //포인터로 선언된 *b 구조체
	(gdb) p *b
	$3 = {_int = 1024, _char = 10 '\n', _double = 3.14 }   //포인터를 사용하여 값 확인
	(gdb) p **b
	Structure has no component named operator*.

### 변수 값 모니터링 하기
원하는 변수의 값이 바뀌는 지점에서 브레이크를 걸려면 와치 포인트 명령어를 사용한다.

	watch [value]
	watch 명령어를 걸어놓은 후 c명령어로 실행시키면
	value값이 바뀔 때 다시 멈춘다.
	ex)
	Old value = 1
	New value = 2
	main () at wz.c:7
	7           i=3;
	(gdb) c
	Continuing.
	Hardware watchpoint 2: i
	Old value = 2
	New value = 3
	main () at wz.c:8
	8           i=0;
	display 화면에 변수값 자동으로 출력하기
	display [변수명]
	s, n, si, ni 등 eip를 진행할 때 마다 변수를 출력하도록 한다.
	display/p, display/x 등 출력 옵션은 p(print)와 동일하다.
	undisplay [display number]로 출력을 종료할 수 있다.

# 변수값 바꾸기

p 명령어로 변수의 값을 바꿀 수 있다.

	p [value]=[바꿀 value];

예를들어, int a = 3이라면
(gdb)p a=10 명령어를 주면 a는 10으로 바뀐다.


# 레지스터 값 보기
	info register (info reg)
	(gdb) info reg
	eax            0xbff23004       -1074647036
	ecx            0xbff22f80       -1074647168
	edx            0x1      1
	ebx            0x639ff4 6529012
	esp            0xbff22f44       0xbff22f44
	ebp            0xbff22f68       0xbff22f68
	esi            0x4f4ca0 5196960
	edi            0x0      0
	eip            0x8048365        0x8048365 <main+17>
	eflags         0x286    [ PF SF IF ]
	cs             0x73     115
	ss             0x7b     123
	ds             0x7b     123
	es             0x7b     123
	fs             0x0      0
	gs             0x33     51
info register $eax 로 원하는것 따로 볼 수 있다.

# 메모리가 가지는 값 확인하기
x 명령어는 메모리 특정 범위의 값들을 확인하는데 사용하는 명령어

***Format letters are o(octal), x(hex), d(decimal), u(unsigned decimal), t(binary), f(float), a(address), i(instruction), c(char), s(string) and z(hex, zero padded on the left). Size letters are b(byte), h(halfword), w(word), g(giant, 8 bytes).*** 

	x/[범위][출력format][단위]
	x/[범위][단위][출력format]

	x/64bx $esp
	:: 스택포인터의 시작지점부터 b(1바이트를) 64번 출력하는데, x(16진수)로 출력

	x/32cw main
	:: 메인함수의 시작지점부터 w(4바이트를) 32번 출력하는데 c(문자열)로 출력
	(gdb) x/16bx $esp
	0xbf94e3f0:     0x00    0x00    0x00    0x00    0x84    0x9a    0x04    0x08
	0xbf94e3f8:     0x08    0xe4    0x94    0xbf    0x41    0x83    0x04    0x08

	print [변수이름]

# 디버깅중인 프로세스에 시그널 보내기

info signals 명령어로 보낼 수 있는 시그널의 종류들을 확인할 수 있음

	signal [SIGNAL]

	ex)   signal SIGALRM
	 signal SIGKILL


# catch
특정 이벤트가 발생했을 때, 프로세스를 중지시킴

```sh
$ gdb -q ./canary
pwndbg> catch syscall arch_prctl
Catchpoint 1 (syscall 'arch_prctl' [158])
pwndbg> run
```



# PLT, GOT
```sh
$ gdb ./got
pwndbg> entry
pwndbg> got
GOT protection: Partial RELRO | GOT functions: 1
[0x404018] puts@GLIBC_2.2.5 -> 0x401030 ◂— endbr64

pwndbg> plt
Section .plt 0x401020-0x401040:
No symbols found in section .plt
pwndbg>
```


# 파이썬과 함께 사용하기

### python argv
	pwndbg> r $(python3 -c "print('\xff' * 100)")
	Starting program: /home/dreamhack/debugee2 
	$(python3 -c "print('\xff' * 100)")
	argv[1] ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ

### python input
	pwndbg> r $(python3 -c "print('\xff' * 100)") <<< $(python3 -c "print('dreamhack')")
	Starting program: /home/dreamhack/debugee2 $(python3 -c "print('\xff' * 100)") <<< $(python3 -c "print('dreamhack')")
	argv[1] ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ
	Name: dreamhack


# pwndbg 고유기능

### telescope
telescope은 pwndbg가 제공하는 강력한 메모리 덤프 기능
특정 주소의 메모리 값들을 보여주는 것에서 그치지 않고, 메모리가 참조하고 있는 주소를 재귀적으로 탐색하여 값을 보여줌

`usage: telescope [-h] [address] [count]`

	pwndbg> tele
	00:0000│ rsp  0x7fffffffc228 —▸ 0x7ffff7a05b97 (__libc_start_main+231) ◂— mov    edi, eax
	01:0008│      0x7fffffffc230 ◂— 0x1
	02:0010│      0x7fffffffc238 —▸ 0x7fffffffc308 —▸ 0x7fffffffc557 ◂— '/home/dreamhack/debugee'
	03:0018│      0x7fffffffc240 ◂— 0x100008000
	04:0020│      0x7fffffffc248 —▸ 0x4004e7 (main) ◂— push   rbp
	05:0028│      0x7fffffffc250 ◂— 0x0
	06:0030│      0x7fffffffc258 ◂— 0x71eb993d1f26e436
	07:0038│      0x7fffffffc260 —▸ 0x400400 (_start) ◂— xor    ebp, ebp

### vmmap
**vmmap**은 가상 메모리의 레이아웃을 보여줌
어떤 파일이 매핑된 영역일 경우, 해당 파일의 경로까지 보여줌

가상 메모리는 물리 메모리와 디스크 공간을 조합하여 프로세스가 더 많은 메모리를 사용하고 
데이터를 효과적으로 관리할 수 있게 해주는 기술

리눅스에서는 ELF를 실행할 때, 먼저 ELF의 코드와 여러 데이터를 가상 메모리에 매핑하고, 
해당 ELF에 링크된 공유 오브젝트(Shared Object, so)를 추가로 메모리에 매핑함

	pwndbg> vmmap
	LEGEND: STACK | HEAP | CODE | DATA | RWX | RODATA
	             Start                End Perm     Size Offset File
	          0x400000           0x401000 r--p     1000      0 /home/dreamhack/debugee
	          0x401000           0x402000 r-xp     1000   1000 /home/dreamhack/debugee
	          0x402000           0x403000 r--p     1000   2000 /home/dreamhack/debugee
	          0x403000           0x404000 r--p     1000   2000 /home/dreamhack/debugee
	          0x404000           0x405000 rw-p     1000   3000 /home/dreamhack/debugee
	          0x405000           0x426000 rw-p    21000      0 [heap]
	    0x7ffff7d7f000     0x7ffff7d82000 rw-p     3000      0 [anon_7ffff7d7f]
	    0x7ffff7d82000     0x7ffff7daa000 r--p    28000      0 /usr/lib/x86_64-linux-gnu/libc.so.6
	    0x7ffff7daa000     0x7ffff7f3f000 r-xp   195000  28000 /usr/lib/x86_64-linux-gnu/libc.so.6
	    0x7ffff7f3f000     0x7ffff7f97000 r--p    58000 1bd000 /usr/lib/x86_64-linux-gnu/libc.so.6
	    0x7ffff7f97000     0x7ffff7f9b000 r--p     4000 214000 /usr/lib/x86_64-linux-gnu/libc.so.6
	    0x7ffff7f9b000     0x7ffff7f9d000 rw-p     2000 218000 /usr/lib/x86_64-linux-gnu/libc.so.6
	    0x7ffff7f9d000     0x7ffff7faa000 rw-p     d000      0 [anon_7ffff7f9d]
	    0x7ffff7fbb000     0x7ffff7fbd000 rw-p     2000      0 [anon_7ffff7fbb]
	    0x7ffff7fbd000     0x7ffff7fc1000 r--p     4000      0 [vvar]
	    0x7ffff7fc1000     0x7ffff7fc3000 r-xp     2000      0 [vdso]
	    0x7ffff7fc3000     0x7ffff7fc5000 r--p     2000      0 /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
	    0x7ffff7fc5000     0x7ffff7fef000 r-xp    2a000   2000 /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
	    0x7ffff7fef000     0x7ffff7ffa000 r--p     b000  2c000 /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
	    0x7ffff7ffb000     0x7ffff7ffd000 r--p     2000  37000 /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
	    0x7ffff7ffd000     0x7ffff7fff000 rw-p     2000  39000 /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
	    0x7ffffffde000     0x7ffffffff000 rw-p    21000      0 [stack]
	0xffffffffff600000 0xffffffffff601000 --xp     1000      0 [vsyscall]
	pwndbg>

# u, nearpc, pdisass(디스어셈블 가독성 향상)
pwndbg에서 제공하는 디스어셈블 명령어


