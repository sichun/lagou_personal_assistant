# -*- coding: utf-8 -*-
import re
import demjson
import pandas as pd
from src.setting import col_names

class JsonParse:
    '''
    解析网页信息
    '''

    def __init__(self, htmlCode):
        self.htmlCode = htmlCode
        self.json = demjson.decode(htmlCode)
        pass

    def parseTool(self, content):
        '''
        清除html标签
        '''
        if type(content) != str: return content
        sublist = ['<p.*?>', '</p.*?>', '<b.*?>', '</b.*?>', '<div.*?>', '</div.*?>',
                   '</br>', '<br />', '<ul>', '</ul>', '<li>', '</li>', '<strong>',
                   '</strong>', '<table.*?>', '<tr.*?>', '</tr>', '<td.*?>', '</td>',
                   '\r', '\n', '&.*?;', '&', '#.*?;', '<em>', '</em>']
        try:
            for substring in [re.compile(string, re.S) for string in sublist]:
                content = re.sub(substring, "", content).strip()
        except:
            raise Exception('Error ' + str(substring.pattern))
        return content

    def parsePage(self):
        '''
        解析并计算页面数量
        :return: 页面数量
        '''
        totalCount = self.json['content']['positionResult']['totalCount']  # 职位总数量
        resultSize = self.json['content']['positionResult']['resultSize']  # 每一页显示的数量
        pageCount = int(totalCount) // int(resultSize) + 1  # 页面数量
        return pageCount

    def parseInfo(self):
        '''
        解析信息
        '''
        info = []
        for position in self.json['content']['positionResult']['result']:
            i = []
            i.append(position['positionId'])
            i.append(position['positionName'])
            i.append(position['salary'])
            i.append(position['workYear'])
            i.append(position['education'])
            i.append(position['jobNature'])
            i.append(position['isSchoolJob'])
            i.append(position['positionAdvantage'])
            i.append(position['firstType'])
            i.append(position['secondType'])
            i.append(position['companyId'])
            i.append(position['companySize'])
            i.append(position['financeStage'])
            i.append(position['industryField'])
            i.append(position['companyShortName'])
            i.append(position['companyFullName'])
            i.append(position['city'])
            i.append(position['district'])
            i.append(position['longitude'])
            i.append(position['latitude'])
            i.append(position['formatCreateTime'])
            i.append(position['resumeProcessRate'])
            i.append(position['resumeProcessDay'])

            info.append(i)
        df = pd.DataFrame(info, columns=col_names)
        return df
