# Give it a try on Python spider
a new-learner spider log, write by CDN.

Might study this at this time: [DouBanSpider/doubanSpider.py](https://github.com/lanbing510/DouBanSpider/blob/master/doubanSpider.py)

#### [db_books]
- 爬取了豆瓣读书top 250的书名和价格信息。
- 思考数据维度的问题：还有什么信息可以拿到？拿到这些数据能干啥？
- 好像没什么能做的了，本来也只是一个练手

#### [antutu_scores]
- 爬取了top50的跑分，用来反映手机性能数据
- 拿不到销量数据很难受。

#### [zol_phones] 
- 只爬取了热门手机榜的第一页，45款机子。
- 没怕后面一页是因为实在...从第二页开始要么是OV要么是others，我感觉没必要了
- 要将zol_phones和antutu_scores联系起来得用到关系数据库，勉强可以用Access混一混，或者直接上MySQL

#### 数据分析
- Python的数据分析方法，回顾大数据经济学的课件与示例代码，~~（可以考虑把那个课件代码搬运到Git上来~~
- R的数据分析方法，主要是数据清洗与计量方法，还得接着复习[DataCamp](https://www.datacamp.com/)

### 接下来：
- 爬取ZOL的品牌数据：[ZOL](http://top.zol.com.cn/compositor/cell_phone.html)
- 销量数据可以考虑淘宝天猫京东，不过这些似乎稍微有点麻烦
- 思考数据维度的问题：拿到这些数据能干啥？
- 学习使用关系数据库MySQL，另找教程
- 待续

#### 一个奇怪的链接
[研发技能表](http://blog.knownsec.com/Knownsec_RD_Checklist/)
