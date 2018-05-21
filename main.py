# -*- coding: utf-8 -*-
from spider.spider import Spider
from preprocess.preprocessor import Prepor
import logging

logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s Process%(process)d:%(thread)d %(message)s',
                    datefmt='%Y-%m -%d %H:%M:%S',
                    filename='diary.log',
                    filemode='a')

if __name__ == '__main__':

    #spider
    import time
    start = time.time()
    kdList = [u'python数据分析']
    cityList = [u'深圳']
    spider = Spider(kdList, cityList)
    spider.main()
    print(time.time()-start)

    # #preprocessing(data statistics & visualization)
    # pre = Prepor("lagou2.csv")
    # pre.process()