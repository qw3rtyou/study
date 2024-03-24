---
sticker: emoji//1f40b
---
# 개념
Dockerfile로 빌드를 하면 이미지를 생성할 수 있음
그러한 이미지로 여러 개의 컨테이너를 만들 수 있고
이미지는 변하지 않음 이미지를 변하게 하려면 빌드를 다시 해야 됨

# 주요 명령어
### 버전 확인	

`docker -v	`

### 빌드
Dockerfile -> 이미지
`-t` 옵션으로 이미지의 이름과 태그를 지정할 수 있음
태그 생략 가능, 생략시 latest로 지정
-f 옵션으로 Dockerfile 위치 설정 가능

`docker build [옵션] [Dockerfile 경로]`
`docker build -t [이미지이름:태그] [도커파일경로] `
`docker build .`
`docker build -t my-image .`

### 이미지 목록 출력
`docker images`

### 이미지 삭제
`docker rmi [옵션] [이미지명|ID]`
 
### 이미지 다운
레지스트리(Docker Hub)에 존재하는 도커 이미지를 다운

`docker pull`
`docker pull ubuntu:18.04`

### 이미지 분석
`docker history [IMAGE_ID]`

이 이상으로 분석하려면 [[dive]]을 이용하는 게 좋


### 컨테이너 생성 및 실행	
이미지 -> 컨테이너
`-p` 옵션은 도커 컨테이너의 포트와 호스트의 포트를 매핑
컨테이너에서 리슨하고 있는 포트를 호스트의 특정 포트로 접속할 수 있도록 함

`docker run [옵션] [이미지명|ID] [명령어]`
`docker run -p [호스트 PORT]:[컨테이너 PORT] [이미지명|ID]`
`docker run --name [컨테이너이름] -it [이미지이름] bash`

`-it` 옵션으로 컨테이너에서 bash 셸을 사용할 수 있음
`-i (--interactive)`는 표준 입력을 활성화하여 사용자가 명령어를 입력할 수 있도록 하고, 
`-t (--tty)`는 가상 터미널(tty)을 사용할 수 있도록 함

`docker run -it [이미지명|ID] [명령어]`
`docker run -it my-image:1 /bin/bash`

백그라운드 실행	
`docker run -d --name 'test1' centos /bin/ping localhost`

### 컨테이너 목록 출력
-a 옵션은 종료된 컨테이너까지 모두 출력
`docker ps -a`

### 컨테이너 생성
`docker create [옵션] [이미지명|ID] [명령어]`

### 컨테이너 실행		
`docker start [컨테이너 이름]`

### 컨테이너 종료
`docker stop [옵션] [컨테이너명|ID]`

### 컨테이너 접속
`docker run`과 유사하게 `-it` 옵션으로 bash 셸을 실행할 수 있음

`docker exec [옵션] [컨테이너명|ID] [명령어]`
`docker exec -it [컨테이너명|ID] /bin/bash`

root로 실행
`docker exec -it --privileged [컨테이너이름] bash`

### 컨테이너 삭제
`docker rm [옵션] [컨테이너명|ID]`

### 컨테이너 및 이미지 정보 출력
`docker inspect [옵션] [이미지 혹은 컨테이너명|ID]`


### 리소스 정리
- 캐시, 디스크 등등 안쓰는 리소스 정리
`docker system prune -a -f` 

- 안쓰는 이미지 정
`docker rmi $(docker images -q) -f`

# Dockerfile
도커 이미지를 빌드하기 위해서는 Dockerfile이 필요
**Dockerfile**은 이미지를 생성하는데 필요한 명령어를 포함하여 모든 설정이 정의된 파일
운영체제와 버전, 환경 변수, 파일 시스템, 사용자 등을 정의

```Dockerfile
# 주석
명령어 인자 
# ---예시---
FROM ubuntu:18.04
```

Dockerfile은 `FROM` 명령어로 시작
이후에는 순서대로 명령어를 실행


## FROM
생성할 이미지의 기반이 되는 base 이미지를 지정함
보통 사용할 운영체제의 공식 이미지를 Dockerhub에서 가져옴

`FROM 이미지:태그`
`FROM ubuntu:18.04`

## ENV
Dockerfile 내에서 사용하는 환경 변수를 지정
파일 내에서 변수는 `$변수명` 혹은 `${변수명}` 형태로 표현

`ENV 변수명 값` or `ENV 변수명=값`
`ENV PYTHON_VERSION 3.11.2` → `.../python/$PYTHON_VERSION/...`

## RUN
이미지를 빌드할 때 실행할 명령어를 작성함
필요한 패키지를 설치하거나, 파일 권한 설정 등의 작업을 수행

`RUN 명령어` or `RUN ["명령어", "인자1", "인자2"]`
`RUN apt-get update`
`RUN ["/bin/bash", "-c", "echo hello"]`

## COPY
src 파일이나 디렉토리를 이미지 파일 시스템의 dst로 복사

`COPY src dst`
`COPY . /app`

## ADD
src 파일이나 디렉토리, URL을 이미지 파일 시스템의 dst로 복사

`ADD src dst`
`ADD . /app`

## WORKDIR
Dockerfile 내의 명령을 수행할 작업 디렉토리를 지정
리눅스의 `cd` 명령어와 유사

`WORKDIR 디렉토리
`WORKDIR /home/user`

## USER

명령을 수행할 사용자 혹은 그룹을 지정

`USER 사용자명|UID` or `USER [사용자명|UID]:[그룹명|GID]`
`USER $username`

## EXPOSE
컨테이너가 실행 중일 때 들어오는 네트워크 트래픽을 리슨할 포트와 프로토콜을 지정
사용할 수 있는 프로토콜은 TCP와 UDP이며, 기본적으로 TCP가 지정

`EXPOSE 포트` or `EXPOSE 포트/프로토콜`
`EXPOSE 80/tcp`


## ENTRYPOINT

`ENTRYPOINT 명령어` or `ENTRYPOINT ["명령어", "인자1", "인자2"]`

컨테이너가 실행될 때 수행할 명령어를 지정합니다.

`ENTRYPOINT ["echo", "hello"]`

## CMD
컨테이너가 실행될 때 수행할 명령어를 지정하거나, `ENTRYPOINT` 명령어에 인자를 전달

`CMD 명령어` or `CMD ["명령어", "인자1", "인자2"]` or `CMD ["인자1", "인자2"]`
`CMD ["echo", "hello"]`

Dockerfile 내에 `CMD` 명령이 여러 개 존재하면 마지막 `CMD`를 사용
`docker run`의 인자를 작성하면 `CMD` 명령어는 무시
`ENTRYPOINT`가 있는 경우, `docker run`의 인자가 `ENTRYPOINT`의 인자로 들어감


Dockerfile이 아래와 같은 경

```Dockerfile
ENTRYPOINT ["python"]
CMD ["app.py"]
```

`docker run [이미지]`로 컨테이너를 실행하면 `python app.py`를 실행
`docker run [이미지] test.py`로 컨테이너를 실행하면 `python test.py`를 실행


# 팁
- 컨테이너 내부에서 `exit` 명령어 사용 시 컨테이너 종료

- docker 내부 파일 수정
```sh
#!/bin/sh
docker run -t -i --rm=true sandbox sh -c "echo 'readme test' > /home/guest/README && /bin/bash"
```

- 어플리케이션 로깅 확인(docker-compose)
```
docker-compose logs app
```

# 실제 사용 스크립트

```
IMAGE_NAME=ubuntu1804 CONTAINER_NAME=my_container;
docker build . -t $IMAGE_NAME;
docker run -d -t --privileged --name=$CONTAINER_NAME $IMAGE_NAME;
docker exec -it -u root $CONTAINER_NAME bash
```

```
docker build . -t fho;
docker run -d -t --privileged --name=fho fho;
docker exec -it -u root fho bash
```
