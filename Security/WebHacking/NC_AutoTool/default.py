import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IP/TCP로 소켓을 생성
server_address = ("127.0.0.1", 7482)  # 접속할 주소와 포트넘버
sock.connect(server_address)  # 생성한 소켓으로 해당 주소에 접속


# 여기서 값을 받는다
recvdata = sock.recv(4096)
print(recvdata.decode())


# 여기서 값을 보내주면 된다다

sent = "What?"

sock.send(sent)


sock.close()
