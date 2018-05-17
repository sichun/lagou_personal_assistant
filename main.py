# -*- coding: utf-8 -*-
from spider.spider import Spider
import logging

logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s Process%(process)d:%(thread)d %(message)s',
                    datefmt='%Y-%m -%d %H:%M:%S',
                    filename='diary.log',
                    filemode='a')

if __name__ == '__main__':
    kdList = [u'自然语言处理']
    cityList = [u'广州', u'成都']
    spider = Spider(kdList, cityList)
    spider.main()