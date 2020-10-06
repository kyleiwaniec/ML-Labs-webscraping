# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 17:17:17 2020

@author: en-chengchang
"""


import requests



#%%  LoginData

session = requests.Session()

headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
loginData = {'fname': 'ml-lab', 'lname': 'ucdcs'}

res = session.post('http://encheng-chang.at.tw/ForTest/test/user_agent.php', data = loginData, headers = headers)
cookies = session.cookies.get_dict()

post_data = {'art': 'My Crawler'}

res = session.post('http://encheng-chang.at.tw/ForTest/test/user_agent_a.php', \
                   headers = headers, \
                   cookies = cookies, \
                   data = post_data)
res.text


