import requests
from bs4 import BeautifulSoup
import re

reqSession = requests.session()
response = reqSession.get("http://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=001&aid=0010197794&date=20180709&type=1&rankingSeq=1&rankingSectionId=101")
soup = BeautifulSoup(response.text,'html.parser')

for i in range(1):
    soupResult = soup.findAll('div', {"class": "article_info"})
    print(str(soupResult))
    exp = r"""(?<=Title">).*(?=</h3>)"""

    rex = re.search(exp, str(soupResult))

    if (rex is not None):
        print(rex.group(0))

