import requests
from pyquery import PyQuery as pq

cookies = {"over18": "1"}
res = requests.get('https://www.ptt.cc/bbs/Gossiping/index.html',
                  cookies = cookies)
mainPageDoc = pq(res.text)