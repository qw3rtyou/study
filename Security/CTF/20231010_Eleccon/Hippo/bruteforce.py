import os
import re

# 현재 디렉토리에서 파일 목록을 얻습니다.
current_directory = os.getcwd()
file_list = os.listdir(current_directory)

# 이메일 주소를 저장할 집합(set)을 생성합니다.
email_addresses = set()

# 중복된 이메일 주소를 저장할 리스트를 생성합니다.
duplicate_emails = []

# 각 파일을 순회하면서 처리합니다.
for file_name in file_list:
    if os.path.isfile(file_name):
        try:
            # 파일을 열고 각 라인을 읽습니다.
            with open(file_name, "r", encoding="utf-8", errors="ignore") as file:
                for line in file:
                    # "From: " 다음의 이메일 주소를 정규 표현식으로 추출합니다.
                    match = re.search(r"From:\s+(.+)", line)
                    if match:
                        email_with_brackets = match.group(1)
                        # 꺾쇠 괄호(<>)를 제외하고 순수한 이메일 주소를 추출합니다.
                        email_match = re.search(r"<(.+)>", email_with_brackets)
                        if email_match:
                            email = email_match.group(1)
                            # 이미 등장한 이메일인 경우 중복 리스트에 저장합니다.
                            if email in email_addresses:
                                duplicate_emails.append(email)
                            else:
                                email_addresses.add(email)
        except Exception as e:
            print(f"Error reading file '{file_name}': {e}")

# 중복된 이메일을 출력하지 않도록 집합(set)에서 제거합니다.
for email in duplicate_emails:
    email_addresses.discard(email)

# 추출된 이메일 주소를 출력합니다.
for email in email_addresses:
    print(email)
