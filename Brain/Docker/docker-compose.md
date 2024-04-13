---
sticker: emoji//1f433
---
# docker-compose
 - 여러 컨테이너를 정의하고 실행하기 위한 도구
 - YAML 파일을 통해 서비스, 네트워크, 볼륨 등을 쉽게 정의하고 관리할 수 있음
 - docker-compose.yml
 - 컨테이너 의존성 관리에 용이

---
# 사용 예시
```
version: '3.8'
services:
  web:
    image: nginx:latest
    ports:
      - "80:80"
    volumes:
      - ./html:/usr/share/nginx/html
    depends_on:
      - db
  db:
    image: postgres:latest
    environment:
      POSTGRES_DB: exampledb
      POSTGRES_USER: exampleuser
      POSTGRES_PASSWORD: examplepass
volumes:
  html:
    driver: local

```

```
version: "3.1"

services:
  php:
    build: .
    ports:
      - "10005:80"
    volumes:
      - ./mysql_info.php:/var/www/config/mysql_info.php
    depends_on:
      - db
    environment:
      MYSQL_DATABASE: ${MYSQL_DATABASE}
      MYSQL_USER: ${MYSQL_USER}
      MYSQL_PASSWORD: ${MYSQL_PASSWORD}

  db:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
      MYSQL_DATABASE: ${MYSQL_DATABASE}
      MYSQL_USER: ${MYSQL_USER}
      MYSQL_PASSWORD: ${MYSQL_PASSWORD}
    volumes:
      - ./sql:/docker-entrypoint-initdb.d

```

- `volumes` 섹션은 컨테이너와 호스트 사이, 또는 여러 컨테이너 간에 영구적으로 저장하고 공유하기 위해 사용됨

---
# 명령어
- 컨테이너 활성화
```
docker-compose up
```

- 컨테이너 비활성화
```
docker-compose down
```


- 어플리케이션 로깅
```
docker-compose logs app
```