---
sticker: emoji//1f5a5-fe0f
---

# 유닉스 계열 공유 폴더 설정

0. vmware 설정에서 공유폴더 설정
1. `vmware-hgfsclient`로 공유폴더 설정이 잘 되었는지 확인
2. `sudo mkdir -p /mnt/shared` 로 마운트할 디렉토리 생성
3. `sudo vmhgfs-fuse .host:/Shared /mnt/shared -o allow_other`로 공유폴더 마운
4.  부팅 시마다 자동으로 마운트하고 싶다면 `.host:/Shared /mnt/shared fuse.vmhgfs-fuse allow_other,defaults 0 0`


# 용량 늘리기
0. vmware 설정에서 원하는 만큼 조정
1. `sudo parted` 에서 `ext4` 와 같은 파일시스템의 Number 확인
2. `resizepart [Number]` 
3. `parted` 명령어에서 나온 후 `sudo resize2fs /dev/sda3`
4. 재부팅

```sh
foo1@foo1-virtual-machine:~$ sudo parted 
GNU Parted 3.4
Using /dev/sda
Welcome to GNU Parted! Type 'help' to view a list of commands.
(parted) print
Model: VMware, VMware Virtual S (scsi)
Disk /dev/sda: 1074GB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags: 

Number  Start   End     Size    File system  Name                  Flags
 1      1049kB  2097kB  1049kB                                     bios_grub
 2      2097kB  540MB   538MB   fat32        EFI System Partition  boot, esp
 3      540MB   644GB   644GB   ext4

(parted) resizepart 3
Warning: Partition /dev/sda3 is being used. Are you sure you want to continue?
Yes/No? yes                                                               
End?  [644GB]? 1000GB                                                     
(parted) print                                                            
Model: VMware, VMware Virtual S (scsi)
Disk /dev/sda: 1074GB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags: 

Number  Start   End     Size    File system  Name                  Flags
 1      1049kB  2097kB  1049kB                                     bios_grub
 2      2097kB  540MB   538MB   fat32        EFI System Partition  boot, esp
 3      540MB   1000GB  999GB   ext4

(parted) 
```

