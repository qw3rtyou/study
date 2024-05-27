- 취약해 보이는 바이너리 3개 선정
1. boa
2. udhcpd
3. miniigd

- 1,2 번은 어느 정도 뭔지는 아는데, miniigd는 잘 모르지만 윈도우 방화벽에서 막길래 한 번 분석해볼 예정 ([Exploit:Linux/CVE-2014-8361.A!xp](!https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?name=Exploit%3ALinux%2FCVE-2014-8361.A!xp&threatid=2147817857))
```
이 취약점은 특히 리얼텍 SDK를 사용하고 miniigd가 있는 다양한 라우터 및 연결된 기기에 영향을 미치며, 원격에서 임의의 코드를 실행할 수 있는 문제를 일으킵니다.

이 취약점의 주된 문제는 인증 없이 원격 코드 실행이 가능하다는 점입니다. 이로 인해 해커들이 장치에 액세스하여 제어할 수 있고, 이를 악용해 대규모 네트워크에서 분산 서비스 거부(DDoS) 공격 같은 악성 활동을 수행할 수 있습니다.
```

---
# boa

## system() 분석


### `sub_438908`
- 분석하기 난해해서 패스


### ~~`sub_436D84`~~
- `formSysLog` 엔드 포인트에서 `submit-url` 파라미터 
- log posioning이랑 command injection이랑 연계 가능해보임
- 상수임 안됨 바보 멍청이
![[Pasted image 20240510114526.png]]

### `sub_4330F8`
- `formWsc` 엔드 포인트에서 `peerRptPin` 파라미터 
- 오커인?
![[Pasted image 20240510114749.png]]

- `formWsc` 엔드 포인트에서 `targetAPSsid` 파라미터 
- 오커인 될 것 같은데 이스케이핑 있음
![[Pasted image 20240510115411.png]]
![[Pasted image 20240510115441.png]]
![[Pasted image 20240510115451.png|300]]

- 이것도 뭔가 가능해 보이는데 잘 모르겠음
![[Pasted image 20240510115832.png]]

	- 대놓고 오커인2
![[Pasted image 20240510134319.png]]

- 대놓고 오커인3
![[Pasted image 20240510134405.png]]
![[Pasted image 20240510134443.png]]


### `sub_432DBC`
- `/tmp`에 접근이 가능하면 command injection 가능해보임
![[Pasted image 20240510113329.png]]


### `sub_42A138`
- `a1` 인자에 뭐가 들어오냐에 따라 오커인이 가능함
- 추후 분석



### `sub_41C9D8`
- 모르겠음 안될것같음



---

# udhcpd

---

# miniigd

