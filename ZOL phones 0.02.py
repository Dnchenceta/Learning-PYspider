# 爬取ZOL手机价格数据，尚未加入翻页
# 这次先不翻页了，ZOL第二页开始的手机都好菜啊，不爬了
# 得到一个top50的phone_df，包括了phone, price, score, com-num

import requests
from bs4 import BeautifulSoup
import re
from pandas import DataFrame

l1 = []
l2 = []
l3 = []
l4 = []
    
url = "http://detail.zol.com.cn/cell_phone_index/subcate57_list_1.html"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;) Gecko/20100101 Firefox/57.0',
               'Host': 'detail.zol.com.cn'}
    
r = requests.get(url, headers = headers)
print(r.status_code)
soup = BeautifulSoup(r.text, "lxml")
    
phone_list = soup.find_all("h3") # 获取手机名称
for each in phone_list:
    a = str(each)
    phone = re.search('title="([^（]*)（(.*)）', a)
    if phone == None:
        pass
    else:
        phone = phone.group(1)
        l1.append(phone)
        
price_list = soup.find_all("b", class_="price-type") # 获取手机价格
for each in price_list:
    price = each.string.strip()
    l2.append(price)
    
score_list = soup.find_all("span", class_="score") # 获取手机评分
for each in score_list:
    score = each.string.strip()
    l3.append(score)
    
com_list = soup.find_all("a", class_="comment-num") # 获取评论人数
for each in com_list:
    num = each.string.strip()
    num = re.match('\d*', num)
    num = num.group()
    l4.append(num)
    
data = {'phone':l1, 'price': l2, 'score': l3, 'com-num': l4}
phone_df = DataFrame(data)
