
# system() 분석


### `sub_438908`
- 분석하기 난해해서 패스


### ~~`sub_436D84`~~
- `formSysLog` 엔드 포인트에서 `submit-url` 파라미터 
- log posioning이랑 command injection이랑 연계 가능해보임
- 상수임 안
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





