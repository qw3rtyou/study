import requests
import json

url = "https://kauth.kakao.com/oauth/token"
client_id = "b07ed7e8ff2727a62608378a990a8281"
redirect_uri = "https://example.com/oauth"
code = "Kyjgl9GvOPJ97Isw_1rG4Jl0kmLzNTHjDWz_UZATHhcJ2SQf9ttHjk4hx18IKDpNo28gkwo9c00AAAGJQj97-g"

data = {
    "grant_type": "authorization_code",
    "client_id": client_id,
    "redirect_uri": redirect_uri,
    "code": code,
}

response = requests.post(url, data=data)
tokens = response.json()

# 발행된 토큰 저장
with open("token.json", "w") as kakao:
    json.dump(tokens, kakao)
