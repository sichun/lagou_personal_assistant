# lagou_personal_assistant
aim to be a personal assistant for finding better jobs


## Code Source
* The code is based on https://github.com/nnngu/LagouSpider
* Add Dataframe to form table structure in order to process data conveniently.
* The job requirement is quite important so that it is necessary to add a new column "jobDescription" with simple cleansing.

## Bug Fixed
**2018-5-17** 
* N/A: every 6 or 7 times get request will be rejected to call. Search the method that using get with cookies.
* Due to good structure, move previous main.py to src/spider.py and initialize a Spider class.
* multi-cities result will be stored in a file.

## Next Step
* basic data statistics, data visualization

## Waiting list 
* data mining
* the speed of spider is too slow