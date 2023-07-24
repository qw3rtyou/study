# 네이티브 앱 키	6fc184eb84e9e5a4b903f2d069aff6c3
# REST API 키	b07ed7e8ff2727a62608378a990a8281
# JavaScript 키	3eca1a8b6aa1f167f151937a60a0f9d4
# Admin 키	0cc8c71922beab54875b5011b8f7b075
# redirect domain  https://example.com/oauth

# https://kauth.kakao.com/oauth/authorize?client_id=b07ed7e8ff2727a62608378a990a8281&redirect_uri=https://example.com/oauth&response_type=code
# https://example.com/oauth?code=Kyjgl9GvOPJ97Isw_1rG4Jl0kmLzNTHjDWz_UZATHhcJ2SQf9ttHjk4hx18IKDpNo28gkwo9c00AAAGJQj97-g


import requests
import json

# 발행한 토큰 불러오기
with open("token.json", "r") as kakao:
    tokens = json.load(kakao)

url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

headers = {"Authorization": "Bearer " + tokens["access_token"]}

for i in range(100):
    data = {
        "object_type": "text",
        "text": "테스트{}".format(i),
        "link": {
            "web_url": "https://developers.kakao.com",
            "mobile_web_url": "https://developers.kakao.com",
        },
        "button_title": "키워드",
    }

    data = {"template_object": json.dumps(data)}
    response = requests.post(url, headers=headers, data=data)
    print(response.status_code)
