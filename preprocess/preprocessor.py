# -*- coding: utf-8 -*-
from preprocess.setting import types
import pandas as pd
import numpy as np
import re

class Prepor:
    def __init__(self, file_name):
        self.data = pd.read_csv(file_name)

    def salary(self):
        sal = self.data['salary'].tolist()
        sal = [re.findall(r'\d+', x) for x in sal]
        np_sal = np.array(sal)
        ##visualization
        # self.salary_visual(np_sal[:, 0], np_sal[:, 1])

        #salary cut to several classes with lagou principle
        low = list(map(int, np_sal[:, 0]))
        salary_cut = pd.cut(low, [2, 5, 10, 15, 25, 50])
        ## 0 is below 5k regarded as intern, which is not important for me.
        salary_class = salary_cut.codes+1

        ## count all classes
        #print(pd.value_counts(salary_cut))

        self.data["salary_class"] = pd.Series(salary_class, index=self.data.index)

    def salary_visual(self, v1, v2):
        from pyecharts import Bar, Grid

        attr = ["{}".format(i) for i in range(len(v1))]
        bar = Bar("salary")
        # 利用第一个 add() 图例的颜色为透明，即 'rgba(0,0,0,0)'，并且设置 is_stack 标志为 True
        bar.add("", attr, v1, label_color=['rgba(0,0,0,0)'], is_stack=True, mark_line=["average"])
        bar.add("", attr, v2, is_label_show=True, is_stack=True)
        bar.render()

        bar2 = Bar("", height=720)
        bar2.add("low", attr, v1, is_stack=True)
        bar2.add("high", attr, v2, is_stack=True)

        grid = Grid()
        grid.add(bar, grid_top="60%")
        grid.add(bar2, grid_bottom="60%")
        grid.render()

    #workYear, companySize, financeStage
    def process_class(self, data, type):
        if type:
            self.data[type] = data.astype(pd.api.types.CategoricalDtype(categories=types[type])).cat.codes
            #print(pd.value_counts(data))

    def process_text(self, data, type, analyst=False):
        #count the words
        #?????synonymy words
        d = {}
        for words in data.tolist():
            if type == "firstType":
                words = words[:-1]
            for word in re.split(',| |，|/', words):
                if analyst:
                    import jieba
                    jieba.load_userdict("preprocess/userdict.txt")
                    for subword in jieba.cut(word):
                        d[subword] = d.get(subword, 0) + 1
                else:
                    d[word] = d.get(word, 0) + 1

        # #wordcloud for visualization
        # self.wordcloud(d.keys(), d.values(), type)

    def wordcloud(self, name, value, type):
        from pyecharts import WordCloud

        wordcloud = WordCloud(width=1300, height=620)
        wordcloud.add(type, name, value, word_size_range=[20, 100])
        wordcloud.render()

    def process(self):
        #temp don't use jieba
        self.process_text(self.data["positionAdvantage"], "positionAdvantage")
        #self.process_text(self.data["secondType"], "secondType", analyst=True)


        # self.salary()
        #
        # self.process_class(self.data["workYear"], "workYear_types")
        # self.process_class(self.data["companySize"], "companySize_types")
        # self.process_class(self.data["financeStage"], "financeStage_types")
        #
        # self.data = pd.get_dummies(self.data, columns=['city'])
        #
        # self.input = self.data.loc[:, ['salary_class', 'workYear_types', 'companySize_types', 'financeStage_types']]
        # df = self.data.filter(regex='city_')
        # self.input = pd.concat([self.input, df], axis=1)
        # print(self.input.head())

    def visual(self):
        # from mpl_toolkits.basemap import Basemap

        # import matplotlib.pyplot as plt
        # # setup Lambert Conformal basemap.
        # m = Basemap(width=1200000, height=900000, projection='lcc',
        #             resolution='c', lat_1=30, lat_0=25, lon_0=113.)
        # ##in order to states shape -> pip install pyshp & download gadm36_CHN_shp
        # m.readshapefile('gadm36_CHN_shp/gadm36_CHN_3', 'states', drawbounds=True)
        # m.shadedrelief()
        #
        # # Map (long, lat) to (x, y) for plotting
        # lon = self.data["longitude"].tolist()
        # print(lon[:3])
        # lat = self.data["latitude"].tolist()
        # x, y = m(lon, lat)
        # plt.plot(x, y, '+r', markersize=5)
        #
        # plt.show()

        ####change use pyecharts for data visualization because of good vision
        # from pyecharts import Geo
        # #pip install pyecharts
        # #pip install echarts-china-provinces-pypkg
        # #pip install echarts-china-cities-pypkg
        # #pip install echarts-countries-pypkg
        #
        # gp = self.data.groupby(by=['city'])
        # cities = self.data['city'].drop_duplicates().tolist()
        # attr = []
        # for city in cities:
        #     if city[-1] != "市":
        #         attr.append(city+'市')
        # value = gp.size().tolist()
        #
        # geo = Geo("工作数量", title_color="#fff",
        #           title_pos="center", width=1200,
        #           height=600, background_color='#404a59')
        # geo.add("", attr, value, visual_range=[0, 20], visual_text_color="#fff",
        #         symbol_size=15, is_visualmap=True, visual_split_number=5)
        # geo.render()
        pass
        #print(self.data.drop_duplicates())