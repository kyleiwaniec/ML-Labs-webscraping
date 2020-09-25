#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 00:13:49 2020

@author: en-chengchang
"""

# =========================================================================== #
#                                                                             #
#                                                                             #
# =========================================================================== #

from selenium import webdriver

# =========================================================================== #
#                                                                             #
#                                                                             #
# =========================================================================== #

CHROME_PATH = '/Users/en-chengchang/Downloads/chromedriver'
WEB_PATH    = 'http://encheng-chang.at.tw/ForTest/test/user_agent.php'
ACCT        = 'ml-lab'
PD          = 'ucdcs'

# =========================================================================== #
#                                                                             #
#                                                                             #
# =========================================================================== #

def get_driver():
    global web_driver
    web_driver = webdriver.Chrome(CHROME_PATH)
    web_driver.get(WEB_PATH)
    web_driver.maximize_window()
    
def give_2_box(kv, value):
    
    if 'id' in kv.keys():
        textbox = web_driver.find_element_by_id(kv['id'])
    elif 'xpath' in kv.keys():
        textbox = web_driver.find_element_by_xpath(kv['xpath'])    
    elif 'name' in kv.keys():
        textbox = web_driver.find_element_by_name(kv['name'])   
    else: 
        raise BaseException('Currently not supported')
    textbox.clear()    
    textbox.send_keys(value)
    
# =========================================================================== #
#                                                                             #
#                                                                             #
# =========================================================================== #    
    
if __name__ == '__main__':
    
    give_2_box({'xpath':'//*[@id="fname"]'}, ACCT)
    give_2_box({'id':'lname'}, PD)
    web_driver.find_element_by_xpath('/html/body/form/input[3]').click()
    
    article = web_driver.page_source