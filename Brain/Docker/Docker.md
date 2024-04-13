---
sticker: emoji//1f40b
---
# 동작 방식
1. [[Dockerfile]]로 빌드를 하면 이미지를 생성할 수 있음
2. 그러한 이미지로 여러 개의 컨테이너를 만들 수 있고
3. 이미지는 변하지 않음 이미지를 변하게 하려면 빌드를 다시 해야 됨

---
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
- 기본 형태
`docker rmi [옵션] [이미지명|ID]`
`-f` 옵션으로 강제로 삭제할 수 있음(사용 중이면 삭제 안됨)

- 이름이 `<none>`인 경우 이를 dangling 이미지라고 하고, 이를 삭제하기 위한 명령어
`docker image prune

- 특정 `<none>`이미지 삭제
`docker rmi <이미지 ID>`

 
### 이미지 다운
레지스트리(Docker Hub)에 존재하는 도커 이미지를 다운

`docker pull`
`docker pull ubuntu:18.04`

### 이미지 분석
`docker history [IMAGE_ID]`

더 자세히 분석하려면 [[dive]]을 이용하는 게 좋음


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
`-d` 백그라운드 실행

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
 

- 안쓰는 이미지 정리
`docker rmi $(docker images -q) -f`


---



# 팁
- 컨테이너 내부에서 `exit` 명령어 사용 시 컨테이너 종료

- docker 이미지 빌드 후 내부 파일 수정
```sh
#!/bin/sh
docker run -t -i --rm=true sandbox sh -c "echo 'readme test' > /home/guest/README && /bin/bash"
```

---
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
