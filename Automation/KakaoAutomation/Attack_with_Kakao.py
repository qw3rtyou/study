import requests
import json


def send_kakao_message(access_token, target_user_id, message):
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    headers = {"Authorization": "Bearer " + access_token}
    data = {
        "template_object": json.dumps(
            {
                "object_type": "text",
                "text": message,
                "link": {"web_url": "https://example.com"},  # 웹 링크 설정 (선택사항)
            }
        )
    }
    params = {"receiver_uuids": '["' + target_user_id + '"]'}

    response = requests.post(url, headers=headers, data=data, params=params)
    if response.status_code == 200:
        print("카카오톡 메시지를 성공적으로 보냈습니다.")
    else:
        print("카카오톡 메시지 전송 실패:", response.json())


# 카카오톡 메시지 보내기
access_token = "YOUR_ACCESS_TOKEN"
target_user_id = "TARGET_USER_ID"  # 수신자 카카오톡 사용자 ID
message = "안녕하세요! 이 메시지는 파이썬에서 보내는 카카오톡 메시지입니다."

send_kakao_message(access_token, target_user_id, message)
