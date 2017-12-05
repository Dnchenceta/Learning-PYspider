import requests
from bs4 import BeautifulSoup
from pandas import DataFrame
import re

list1 = []
list3 = []
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;) Gecko/20100101 Firefox/57.0',
               'Host': 'book.douban.com'}
for i in range(0, 10):
    link = "http://book.douban.com/top250?start=" + str(i*25)
    r = requests.get(link, headers = headers, timeout = 10)
    print(str(i+1), 'status code:', r.status_code)
    
    soup = BeautifulSoup(r.text, 'lxml')
    
    title_list = soup.find_all('div', class_= 'pl2') # 生成书名信息
    for each in title_list:
        title = each.a.text.strip()
        c = re.sub('[\n\s]*', '', title)
        list1.append(c)
        
    price_list = soup.find_all('p', class_= 'pl') # 生成价格信息
    for each in price_list:
        price = re.search("\d-{0,}\S / \D*[\d.]{1,}", str(each))
        a = re.search("/ \d*", str(price))
        b = a.group()
        b = b[2:]
        list3.append(b)
    
data = {'title':list1, 'price': list3}
book_df = DataFrame(data)

sum(book_df['price'] == '')
sum(book_df['price'] == '0')
