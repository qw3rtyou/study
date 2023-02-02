import requests
from bs4 import BeautifulSoup as bs
from openpyxl import Workbook

wb=Workbook(write_only=True)
ws=wb.create_sheet('TV Ratings')
ws.append(['순위','채널','프로그램','시청률'])

page=requests.get("https://workey.codeit.kr/ratings/index").text

soup=bs(page,'html.parser')
for tr_tag in soup.select('tr')[1:]:
    td_tags=tr_tag.select('td')
    row=[
        td_tags[0].get_text(),
        td_tags[1].get_text(),
        td_tags[2].get_text(),
        td_tags[3].get_text()
    ]
    ws.append(row)
    
print(ws)

wb.save('시청률.xlsx')