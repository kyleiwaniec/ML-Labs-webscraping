#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 10:38:22 2020

@author: en-chengchang
"""

# =========================================================================== #
#                                                                             #
#                                                                             #
# =========================================================================== #

from tqdm import tqdm
from selenium import webdriver
import pandas as pd
import re
import os

# =========================================================================== #
#                                                                             #
#                                                                             #
# =========================================================================== #

CHROME_PATH     = '/Users/en-chengchang/Downloads/chromedriver'
OUTPUT_PATH     = '/Users/en-chengchang/Desktop/bootcamp/PeerLearning/ML-Labs-webscraping/Data/'
CATEGORY_URL    = 'http://www.thetruthseeker.co.uk/?page_id=12'
MAIN_PAGE_PAT   = 'http://www.thetruthseeker.co.uk/?p='
RESCRAPE_URL    = True
RESCRAPE_POSTS  = True
MAX_PAGE        = 20

# =========================================================================== #
#                                                                             #
#                                                                             #
# =========================================================================== #

def explore_accesible_posts():
    try: os.remove(OUTPUT_PATH + 'truthSeekerURL.txt')
    except: pass
    
    web_driver = webdriver.Chrome(CHROME_PATH)
    web_driver.get(CATEGORY_URL)
    page_source = web_driver.page_source
    category_set = re.findall('http://www.thetruthseeker.co.uk/\?cat=[0-9]+', page_source)
    
    
    for category in tqdm(category_set):
          
        page = 1
        while True:
            web_driver.get(category +'&paged='+ str(page))
            page_source = web_driver.page_source
            access_p = re.findall('div id="post-([0-9]+)', page_source)  

            if access_p == ['0'] or page == MAX_PAGE + 1:  break
            else: page += 1
            
            with open(OUTPUT_PATH + 'truthSeekerURL.txt', 'a+') as files: 
                files_content = files.read()
                files.write(files_content + '\n')
                files.write('\n'.join([MAIN_PAGE_PAT + i for i in access_p]))
    web_driver.close()
    
    
def scrape_posts():
    try: os.remove(OUTPUT_PATH + 'truthSeekerCont.txt')
    except: pass

    with open(OUTPUT_PATH + 'truthSeekerURL.txt', 'r') as files: 
        files_content = files.read()
        files_content = [i for i in files_content.split('\n') if i != '']
    
    web_driver = webdriver.Chrome(CHROME_PATH)
    
    for url in tqdm(files_content):
        web_driver.get(url)    
        
        post_num = re.search('=([0-9]+)', url).group(1)
        try:
            title = web_driver.find_element_by_xpath('//*[@id="post-{0}"]/h1'.format(post_num)).text
            time = web_driver.find_element_by_xpath('//*[@id="post-{0}"]/p[1]/abbr'.format(post_num)).text
            article = web_driver.find_element_by_xpath('//*[@id="post-{0}"]/div'.format(post_num)).text
            with open(OUTPUT_PATH + 'truthSeekerCont.txt', 'a+') as files: 
                files_content = files.read()
                files.write('\x01'.join([title, time, article]) + '\x02')
        except: continue
    

def txt2csv():
    with open(OUTPUT_PATH + 'truthSeekerCont.txt', 'r') as files: 
        files_content = files.read()
        files_content = [i.split('\x01') for i in files_content.split('\x02')][:-1]
    data = pd.DataFrame(files_content, columns = ['Title', 'Date', 'Article'])
    data.to_csv(OUTPUT_PATH + 'truthSeekerData.csv', index = False, encoding = 'utf-8')
    
# =========================================================================== #
#                                                                             #
#                                                                             #
# =========================================================================== #    
    
if __name__ == '__main__':
    
    if RESCRAPE_URL == True:
        explore_accesible_posts()
        
    if RESCRAPE_POSTS == True:
        scrape_posts()
        
    txt2csv()
