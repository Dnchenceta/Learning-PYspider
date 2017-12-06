import requests
from bs4 import BeautifulSoup
import re
from pandas import DataFrame

def get_phones():
    
    l1 = []
    l2 = []
    
    url = "http://www.antutu.com/ranking/rank1.htm"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0",
              "Host": "www.antutu.com"}
    
    r = requests.get(url, headers = headers)
    soup = BeautifulSoup(r.text, "lxml")
    
    phone_list = soup.find_all("div", class_="attrs") # 获取手机名称
    for each in phone_list:
        phone = each.string.strip()
        l1.append(phone)
    
    score_list = soup.find_all("div", class_= "score-num") # 获取跑分数值
    for each in score_list:
        sco = each.string.strip()
        l2.append(sco)
        
    data = {'phone': l1, 'score': l2}
    phone_df = DataFrame(data)
    
    return(phone_df)
    
get_phones()
