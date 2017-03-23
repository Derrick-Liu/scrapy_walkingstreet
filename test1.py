#coding:utf-8

import requests
from lxml import etree

url='https://my.hupu.com/er_yuan_hua_shi/profile'

cookie={'cookies':'_cnzz_CV30020080=buzi_cookie%7Cd0365e70.5594.0c09.a95c.0f8617507ae5%7C-1; PHPSESSID=v7aos12hl11f6cnff7ceqhkgk1; _dacevid3=d0365e70.5594.0c09.a95c.0f8617507ae5; _HUPUSSOID=c8dae74b-965c-4db6-b5ed-0d29295ac719; _cnzz_CV30020080=buzi_cookie%7Cd0365e70.5594.0c09.a95c.0f8617507ae5%7C-1; AUM=dgic8aVaD0I9XtKH8-GYD7O3jN5nt-yqlWtWpTno5j7lw; _CLT=918ebe7bb324d8673460f7af1d701a5c; u=18555774|bGl1c2hpbGx5|b91a|47f494930255b895393f54a4a7e9a5ec|0255b895393f54a4|bGl1c2hpbGx5; ua=19863476; us=c5823cb1d07422b569c4a3520f41484bdb70087803c365cb0af228b5c823243b9b2eb4ee6eda701e6afd5b0e6681d8a311b3487dd0927cdf8524d5214f5e23c6; __dacevst=320603d9.3c16139d|1489762498436'}
html=requests.get(url,cookies=cookie).content

selector=etree.HTML(html)
gender=selector.xpath('//*[@id="content"]/table[1]/tr[1]/td[2]/text()')
name=selector.xpath('//*[@id="headtop"]/h1/text()')



print html
print len(html)
print gender[0]
print name[0]