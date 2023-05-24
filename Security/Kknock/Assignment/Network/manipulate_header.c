#include <stdio.h>
#include <winsock2.h>

#pragma comment(lib, "ws2_32.lib")

int main() {
    // 윈속 초기화
    WSADATA wsa;
    if (WSAStartup(MAKEWORD(2, 2), &wsa) != 0) {
        printf("윈속 초기화 실패\n");
        return 1;
    }
    
    // 소켓 생성
    SOCKET sockfd = socket(AF_INET, SOCK_STREAM, 0);

    // 서버 정보 설정
    struct sockaddr_in server;
    server.sin_family = AF_INET;
    server.sin_port = htons(3737);  // HTTP 포트 번호
    server.sin_addr.s_addr = inet_addr("20.200.213.238");

    // 서버에 연결
    if (connect(sockfd, (struct sockaddr*)&server, sizeof(server)) < 0) {
        printf("서버 연결 실패\n");
        return 1;
    }

    // HTTP 요청 메시지 생성
    char request[1024];
    snprintf(request, sizeof(request), "GET / HTTP/1.1\r\n"
                                        "Host: 20.200.213.238\r\n"
                                        "User-Agent: admin\r\n"
                                        "Cookie: Choi Jeong Won\r\n"
                                        "\r\n");

    // 서버로 요청 전송
    send(sockfd, request, strlen(request), 0);

    // 응답 수신 및 출력
    char response[4096];
    memset(response, 0, sizeof(response));
    recv(sockfd, response, sizeof(response) - 1, 0);
    printf("%s\n", response);

    // 소켓 닫기
    closesocket(sockfd);

    // 윈속 해제
    WSACleanup();

    return 0;
}