import http.server
import socketserver
import socket

class ProxyHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # 클라이언트 요청 수신
        request = self.request.recv(4096)
        
        # 요청 헤더 수정
        request_str = request.decode('utf-8')
        headers = request_str.split('\r\n\r\n')[0].split('\r\n')
        modified_headers = []

        for header in headers:
            if header.startswith('User-Agent:'):
                modified_headers.append('User-Agent: admin')
                modified_headers.append('Cookie: Choi Jeong Won')
            else:
                modified_headers.append(header)

        modified_request_str = '\r\n'.join(modified_headers) + '\r\n\r\n'
        modified_request = modified_request_str.encode('utf-8')
        
        # 원격 서버로 수정된 요청 전송
        remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        remote_socket.connect(('20.200.213.238', 3737))
        remote_socket.send(modified_request)
        
        # 원격 서버로부터 응답 수신
        response = remote_socket.recv(4096)
        
        # 클라이언트로 수정된 응답 전송
        self.request.sendall(response)

# 프록시 서버 설정
host = "127.0.0.1"
port = 8888

# 프록시 서버 실행
with socketserver.ThreadingTCPServer((host, port), ProxyHandler) as server:
    print(f"Proxy server is running on {host}:{port}")
    server.serve_forever()