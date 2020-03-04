#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
import pandas as pd
from pyquery import PyQuery as pq
import datetime
from IPython.display import Image


# In[4]:


def craw():
    now=datetime.datetime.now()
    headers={'User-Agent':'Mozilla/5.0'}
    momo_res=requests.get('https://www.momoshop.com.tw/edm/cmmedm.jsp?lpn=O1Htnu33wrO&n=',headers=headers)
    momo_doc=pq(momo_res.text)
    coupon_list=[]
    description_list=[]
    time_list=[]
    for each in momo_doc('.coupArea').items():
        coupon=each.text().split('\n')[0]
        time=each.text().split('\n')[-1][3:]
    #     效期
        ending=time.split('-')[-1]
    #     效期最後一日

        if len(each.text().split('\n'))==4:   
            coupon+=each.text().split('\n')[1]
            description=each.text().split('\n')[2]
        else:
            description=each.text().split('\n')[1]

            # 有些折價券時效不只有日期還有時間
        if '點' in ending:
            date_ending=datetime.datetime.strptime(ending,'%Y/%m/%d %H點')
        else:
            one_day=datetime.timedelta(days=1)
            date_ending=datetime.datetime.strptime(ending,'%Y/%m/%d')
            date_ending+=one_day

        if now<date_ending:
    #         抓下來的資料中若有'奇怪的'折價券不在網頁中,用if 剔除
            if coupon!='折價券 $':
                time_list.append(time)
                coupon_list.append(coupon)
                description_list.append(description)
    table={"折價券":coupon_list,'屬性':description_list,'效期':time_list}

    df = pd.DataFrame(table)
    df.set_index("折價券", inplace =True)
    return df


# In[11]:


# 銀行優惠
def bank():
    now=datetime.datetime.now()
    headers={'User-Agent':'Mozilla/5.0'}
    momo_res=requests.get('https://www.momoshop.com.tw/edm/cmmedm.jsp?lpn=O1Htnu33wrO&n=',headers=headers)
    momo_doc=pq(momo_res.text)
    bank_url=momo_doc('#BodyBase > div:nth-child(4) > div > div:nth-child(4) > div > div.mainArea > div.more > a').attr('href')
    bank_res=requests.get(bank_url,headers=headers)
    bank_doc=pq(bank_res.text)
    image_url_list=[]
    for each in bank_doc('.banklogo > img').items():
        image=each.attr('src')
        image_url_list.append(image)
    contxt_list=[]
    for each in bank_doc('.contxt').items():
        contxt_list.append(each.text().split())
    for each in contxt_list:
        while '額滿' in each:
            each.pop(each.index('額滿')+1)
            each.remove('額滿')        
    index=0
    for each in contxt_list:
        each.insert(0 , image_url_list[index])
        index+=1
        if len(each)==1:
            each.append('全部額滿')
#     return contxt_list
    outputList = []
    for each in contxt_list:
        instanceList = []
        instanceList.append(each[0])
        instanceList.append('\n'.join(each[1:]))
    #     display(Image(url=each[0]))
        outputList.append(instanceList)
#         outputList.append('\n'.join(each[1:]))
    return outputList
# print(bank())


# In[25]:




