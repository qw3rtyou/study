# 개념
Dockerfile로 빌드를 하면 이미지를 생성할 수 있음
그러한 이미지로 여러개의 컨테이너를 만들 수 있고
이미지는 변하지 않음 이미지를 변하게 하려면 빌드를 다시해야됨

# cmd
버전 확인		docker -v	
도커 빌드		docker build -t 이미지이름 도커파일경로
도커 실행		docker run --name 컨테이너이름 -it 이미지이름 bash
도커 실행(root)	docker exec -it --privileged 컨테이너이름 bash
백그라운드 실행	docker run -d --name 'test1' centos /bin/ping localhost
컨테이너 실행		docker start [컨테이너 이름]
컨테이너 확인		docker ps