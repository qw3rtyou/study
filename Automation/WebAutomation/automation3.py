#-*- coding: utf-8 -*-

from openpyxl import Workbook
import requests
from bs4 import BeautifulSoup as bs

wb=Workbook(write_only=True)
ws=wb.create_sheet('sbs')
ws.append(['기간','순위','프로그램','시청률'])

#year=2010&month=1&weekIndex=0

for year in range(2010,2019):
    for month in range(1,13):
        for index in range(0,5):
            page=requests.get('https://workey.codeit.kr/ratings/index?year={}&month={}&weekIndex={}'.format(year,month,index)).text
            soup=bs(page,'html.parser')
            
            for tr_tag in soup.select('tr')[1:]:
                td_tag=tr_tag.select('td')
                
                if td_tag[1].get_text().strip()=='SBS':
                    period='{} 년 {} 월 {}주차'.format(year,month,index+1)
                    rank=td_tag[0].get_text()
                    program=td_tag[2].get_text()
                    percent=td_tag[3].get_text()

                    ws.append([period,rank,program,percent])
            
wb.save('SBS_data.xlsx')