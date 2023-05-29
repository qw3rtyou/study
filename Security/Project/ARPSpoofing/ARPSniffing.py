from scapy.all import *
from scapy.layers.inet import IP

victimip = "172.30.1.23"
serverip = "172.30.1.1"


def packet_handler(packet):
    if packet.haslayer(IP):
        print(packet.summary())
        # if packet[IP].src == serverip and packet[IP].dst == victimip:
        #     # 서버에서 피해자로 가는 패킷을 가로채고 처리
        #     print("서버에서 피해자로 가는 패킷을 가로채고 처리:", packet.summary())

        # elif packet[IP].src == victimip and packet[IP].dst == serverip:
        #     # 피해자에서 서버로 가는 패킷을 가로채고 처리
        #     print("피해자에서 서버로 가는 패킷을 가로채고 처리:", packet.summary())


def packet_sniffer():
    try:
        sniff(prn=packet_handler, filter="ip")
    except KeyboardInterrupt:
        print("패킷 스니핑 종료")


def main():
    # 패킷 스니핑 스레드 시작
    sniff_thread = threading.Thread(target=packet_sniffer)
    sniff_thread.daemon = True  # 데몬 스레드로 설정
    sniff_thread.start()

    try:
        while True:
            print("프로그램이 실행 중입니다...")
            time.sleep(5)  # 5초 대기
            pass
    except KeyboardInterrupt:
        print("패킷 스니핑 종료")


if __name__ == "__main__":
    main()
