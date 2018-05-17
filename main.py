# -*- coding: utf-8 -*-
from src.https import Http
from src.jsonparse import JsonParse
from src.setting import headers
from src.setting import cookies
import time
import logging
import pandas as pd
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s Process%(process)d:%(thread)d %(message)s',
                    datefmt='%Y-%m -%d %H:%M:%S',
                    filename='diary.log',
                    filemode='a')

def getInfo(url, para):
    """
    获取信息
    """
    generalHttp = Http()
    htmlCode = generalHttp.post(url, para=para, headers=headers, cookies=cookies)
    generalParse = JsonParse(htmlCode)
    pageCount = generalParse.parsePage()
    df = pd.DataFrame()
    for i in range(1, pageCount + 1):
        print('第%s页' % i)
        para['pn'] = str(i)
        htmlCode = generalHttp.post(url, para=para, headers=headers, cookies=cookies)
        generalParse = JsonParse(htmlCode)
        df2 = generalParse.parseInfo()
        df = pd.concat([df, df2], ignore_index=True)
        time.sleep(2)
    return df

def getInfoMore(info):
    positionId = info.iloc[:, 0]
    generalHttp = Http()
    text=[]
    for id in positionId:
        url = r'http://www.lagou.com/jobs/%s.html' % id
        html = generalHttp.get(url)
        text.append(getInfoDetail(html)) #return 职业描述 任职要求
    stext = pd.Series(text)
    info['jobDescription'] = stext.values
    return info

def getInfoDetail(content):
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




def processInfo(info):
    """
    信息存储
    """
    logging.error('Process start')
    try:
        info.to_csv("lagou.csv")
        return True
    except Exception as e:
        print(e)
        return None


def main(url, para):
    """
    主函数逻辑
    """
    logging.error('Main start')
    if url:
        info = getInfo(url, para)  # 获取json信息
        info = getInfoMore(info) #get job description
        flag = processInfo(info)  # 信息储存
        return flag
    else:
        return None


if __name__ == '__main__':
    kdList = [u'自然语言处理']
    cityList = [u'广州']
    url = 'https://www.lagou.com/jobs/positionAjax.json'
    for city in cityList:
        print('爬取%s' % city)
        para = {'first': 'true', 'pn': '1', 'kd': kdList[0], 'city': city}
        flag = main(url, para)
        if flag:
            print('%s爬取成功' % city)
        else:
            print('%s爬取失败' % city)
