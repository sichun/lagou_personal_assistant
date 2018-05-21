# lagou_personal_assistant
aim to be a personal assistant for finding better jobs


## Code Source
* The code is based on https://github.com/nnngu/LagouSpider
* Add Dataframe to form table structure in order to process data conveniently.
* The job requirement is quite important so that it is necessary to add a new column "jobDescription" with simple cleansing.

## Bug Fixed
**2018-5-17** 
* N/A: every 6 or 7 times get request will be rejected to call. Search the method that use get with cookies.
* Due to good structure, move previous main.py to src/spider.py and initialize a Spider class.
* multi-cities result will be stored in a file.

``The first stage of spider is completed``

**2018-5-18**
* map visualization: install basemap(https://github.com/matplotlib/basemap)

The map visualization is poor pixel so that I change to other libraries.
(https://zhuanlan.zhihu.com/p/28828483)
Because I have a little experience of Echarts, the open source "pyecharts" is a good choice.

**2018-5-21**
* focus on converting categorical data(workYear, companySize, financeStage, city) to number.
reference: http://benalexkeen.com/mapping-categorical-data-in-pandas/
* salary data transform and visualization.
* wordcloud: count words https://codeburst.io/python-basics-11-word-count-filter-out-punctuation-dictionary-manipulation-and-sorting-lists-3f6c55420855


## Next Step
* basic data selection, statistics, data visualization
* text mining 

## Waiting list 
* data mining
* the speed of spider is too slow
* the output of pycharts is a html file
* when the company is built 