import requests
from bs4 import BeautifulSoup
import re
import csv
import json


url ="http://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=001&aid=0010197793&date=20180709&type=1&rankingSeq=1&rankingSectionId=101"

class newsCrawling:
    def __init__(self):

        self.reqSession = requests.session()
        self.response = self.reqSession.get(url)
        self.soup = BeautifulSoup(self.response.text, 'html.parser')
        self.rex = 0

    def startCrawling(self):

        print("크롤링 하는중...")

        for i in range(10):

            self.exp = r"""(?<=Title">).*(?=</h3>)"""
            self.soupResult = self.soup.findAll('div', {"class": "article_info"})
            #print(str(soupResult))

            self.rex = re.search(self.exp, str(self.soupResult[0]))

        print("크롤링 끝")

    def saveDataCSV(self):
        print("CSV로 파일 저장하는중...")

        if (self.rex is not None):
            self.csvfile = open('news title.csv', 'w')


            self.spamWriter = csv.writer(self.csvfile)
            self.spamWriter.writerow([str(self.rex.group(0))])

        print("CSV로 파일 저장 완료")



    def saveDataJSON(self):
        print("JSON으로 파일 저장 하는중...")
        self.jsonfile = open('news title.json', 'w')

        if (self.rex is not None):

            self.title = self.rex.group(0)
            self.data = {"title": str(self.rex.group(0))}
            json.dump(self.data, self.jsonfile)

            print("JSON으 로 파일 저장 완료")







a = newsCrawling()
a.startCrawling()
a.saveDataCSV()
a.saveDataJSON()


