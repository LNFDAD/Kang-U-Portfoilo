
import requests
from bs4 import BeautifulSoup
import time

json = requests.get('https://www.naver.com/srchrank?frm=main').json()

ranks = json.get("data")
f = open('Python\\navertop\\_네이버실검.txt', 'w')
header = '"네이버 실검 TOP20" ( ' + time.strftime('%Y-%m-%d / %X', time.localtime(time.time())) + ' )\n============================================================\n'
f.write(header)
for r in ranks:
    rank = r.get("rank")
    keyword = r.get("keyword")
    data = str(rank) + '.'+' ' + keyword +'\n'
    f.write(data)
f.write("============================================================\n Copyright 2020. Kangyoo all rights reserved. / Made By Kangyoo (https://www.naver.com/)")
f.close()

