#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from pyquery import PyQuery as pq
import pandas as pd


# In[7]:





# In[3]:


def crawler():
    response = requests.get("https://tw.buy.yahoo.com/coupons?guccounter=1")
    doc = pq(response.text)
    limitList = []
    moneyList = []
    nameList = []
    dateList = []
    for each in doc('#isoredux-root > div > div.CouponsList__content___1VcDX > div.CouponsList__rightBox___3qndK > div > div:nth-child(n+2) > div > div.CouponsItem__facade___1rl5N.CouponsItem__pinkBg___2uEFN >\
    div.CouponsItem__info___Cx9jd.CouponsList__info___keAxm').items():
    #     print(each.text())
    #     print(each(".CouponsItem__description___3AL-j").text())
        limitList.append(each(".CouponsItem__description___3AL-j").text())
        moneyList.append(each(".CouponsItem__price___ehWTy").text())
        nameList.append(each(".CouponsItem__title___3YAqx").text())
        dateList.append(each(".CouponsItem__duration___1fssD").text())
    # print(nameList)
    alldict = {"優惠券名稱" : nameList, "金額" : moneyList,"條件" : limitList, "期限" : dateList}
    # money = {"金額" : moneyList}
    # name = {"優惠券名稱" : nameList}
    # date = {"期限" : dateList}

    df = pd.DataFrame(alldict)
    df.set_index("優惠券名稱", inplace= True)
    return df

#     df.to_csv(r'pandas.txt', sep=' ', mode='a')
    # df.to_html('file.html')


# In[4]:


def imgUrl():
    response = requests.get("https://tw.buy.yahoo.com/activity/activity950?p=all2-00-090316-credit-card")
    doc = pq(response.text)
    totalList = []
    
#     textList = []
    for each in doc("div.C321B2_R_TB ").items():
        instanceList = []
        url = each("div.C321B2_logo > span > img").attr("src")
        instanceList.append(url)
    #     print(each("div.C321B2_text").text())
        instanceList.append(each("div.C321B2_text").text())
        totalList.append(instanceList)
    for each in doc("div.C321B2_L_TB ").items():
        instanceList1 = []
        url = each("div.C321B2_logo > span > img").attr("src")
        instanceList1.append(url)
    #     print(each("div.C321B2_text").text())
        instanceList1.append(each("div.C321B2_text").text())
        totalList.append(instanceList1)
#     for each in doc("div.C321B2_R_TB").items():
#     #     print(each.text())
        
#     for each in doc("div.C321B2_L_TB").items():
       
    return totalList
# print(imgUrl())


# In[3]:


# def content():
#     response = requests.get("https://tw.buy.yahoo.com/activity/activity950?p=all2-00-090316-credit-card")
#     doc = pq(response.text)
        
#     return textList
# # print(content())

