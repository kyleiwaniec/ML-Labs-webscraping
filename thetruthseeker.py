#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 10:38:22 2020

@author: Long Mai
"""

# =========================================================================== #
#                                                                             #
#                                                                             #
# =========================================================================== #

from tqdm import tqdm
import pandas as pd
import re
import os
from bs4 import BeautifulSoup
import requests

# =========================================================================== #
#                                                                             #
#                                                                             #
# =========================================================================== #

OUTPUT_PATH     = './Data/'
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
    
    page_source = requests.get(CATEGORY_URL).text
    category_set = re.findall('http://www.thetruthseeker.co.uk/\?cat=[0-9]+', page_source)
    
    for category in tqdm(category_set):
          
        page = 1
        while True:
            page_source = requests.get(category +'&paged='+ str(page)).text
            access_p = re.findall('div id="post-([0-9]+)', page_source)  

            if access_p == ['0'] or page == MAX_PAGE + 1:  break
            else: page += 1
            
            with open(OUTPUT_PATH + 'truthSeekerURL.txt', 'a+') as files: 
                files_content = files.read()
                files.write(files_content + '\n')
                files.write('\n'.join([MAIN_PAGE_PAT + i for i in access_p]))
    
    
def scrape_posts():
    try: os.remove(OUTPUT_PATH + 'truthSeekerCont.txt')
    except: pass

    with open(OUTPUT_PATH + 'truthSeekerURL.txt', 'r') as files: 
        files_content = files.read()
        files_content = [i for i in files_content.split('\n') if i != '']
    
    for url in tqdm(files_content):
        post_num = re.search('=([0-9]+)', url).group(1)
        raw_html = requests.get('http://www.thetruthseeker.co.uk/?p=' +str(post_num)).text
        tree = BeautifulSoup(raw_html,'lxml')
        
        try:
            title = tree.find("h1",{"class": "post-title entry-title"}).text
            article = tree.find("div",{"class": "entry-content"}).text
            sub_tree = tree.find("div",{"id": "post-" + str(post_num)})
            time = sub_tree.find("abbr",{"class": "published"}).text            
            with open(OUTPUT_PATH + 'truthSeekerCont.txt', 'a+') as files: 
                files_content = files.read()
                files.write('\x01'.join([title, time, article]) + '\x02')
        except: continue
    

def txt2xlsx():
    with open(OUTPUT_PATH + 'truthSeekerCont.txt', 'r') as files: 
        files_content = files.read()
        files_content = [i.split('\x01') for i in files_content.split('\x02')][:-1]
    data = pd.DataFrame(files_content, columns = ['Title', 'Date', 'Article'])
    data.to_excel(OUTPUT_PATH + 'truthSeekerData.xlsx', index = False, encoding = 'utf-8')
    
# =========================================================================== #
#                                                                             #
#                                                                             #
# =========================================================================== #    
    
if __name__ == '__main__':
    
    if RESCRAPE_URL == True:
        explore_accesible_posts()
        
    if RESCRAPE_POSTS == True:
        scrape_posts()
        
    txt2xlsx()
