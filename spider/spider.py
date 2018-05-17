# -*- coding: utf-8 -*-
from spider.https import Http
from spider.jsonparse import JsonParse
from spider.setting import headers
from spider.setting import cookies
import time
import logging
import pandas as pd
from bs4 import BeautifulSoup

class Spider:
    def __init__(self,kdList, cityList):
        self.kdList = kdList
        self.cityList = cityList
        self.url = 'https://www.lagou.com/jobs/positionAjax.json'
        self.df = pd.DataFrame()

    def getInfo(self, url, para):
        """
        获取信息
        """
        generalHttp = Http()
        htmlCode = generalHttp.post(url, para=para, headers=headers, cookies=cookies)
        generalParse = JsonParse(htmlCode)
        pageCount = generalParse.parsePage()
        for i in range(1, pageCount + 1):
            print('第%s页' % i)
            para['pn'] = str(i)
            htmlCode = generalHttp.post(url, para=para, headers=headers, cookies=cookies)
            generalParse = JsonParse(htmlCode)
            df2 = generalParse.parseInfo()
            self.df = pd.concat([self.df, df2], ignore_index=True)
            time.sleep(2)

    def getInfoMore(self):
        positionId = self.df.iloc[:, 0]
        generalHttp = Http()
        text=[]
        for ix, id in enumerate(positionId):
            url = r'http://www.lagou.com/jobs/%s.html' % id
            html = generalHttp.get(url, cookies=cookies)
            text.append(self.getInfoDetail(html)) #return 职业描述 任职要求
        stext = pd.Series(text)
        self.df['jobDescription'] = stext.values

    def getInfoDetail(self, content):
        """
        信息解析
        """
        soup = BeautifulSoup(content, features='lxml')
        jd = []
        try:
            for job_description in soup.find("dd", class_ = "job_bt").find_all("p"):
               jd.append(job_description.text)
            #暂时使用newline作为分割，需要再cleansing
            return "\n".join(jd)
        except:
            return "N/A"




    def processInfo(self):
        """
        信息存储
        """
        logging.error('Process start')
        try:
            self.df.to_csv("lagou.csv")
            return True
        except Exception as e:
            print(e)
            return None


    def main(self):
        """
        主函数逻辑
        """
        logging.error('Main start')

        for city in self.cityList:
            print('爬取%s' % city)
            para = {'first': 'true', 'pn': '1', 'kd': self.kdList[0], 'city': city}
            if self.url:
                self.getInfo(self.url, para)  # 获取json信息
            else:
                flag = None
        self.getInfoMore()  # get job description
        flag = self.processInfo()  # 信息储存
        if flag:
            print('%s爬取成功' % city)
        else:
            print('%s爬取失败' % city)
