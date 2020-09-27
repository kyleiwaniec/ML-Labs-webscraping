#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 23:12:37 2020

@author: en-chengchang
"""

# =========================================================================== #
#                                                                             #
#                                                                             #
# =========================================================================== #

from time import sleep
from selenium import webdriver
from PIL import Image
import platform

# =========================================================================== #
#                                                                             #
#                                                                             #
# =========================================================================== #

CHROME_PATH     = '/Users/en-chengchang/Downloads/chromedriver'
OUTPUT_PATH     = '/Users/en-chengchang/Desktop/bootcamp/PeerLearning/ML-Labs-webscraping/Data/IMG'
WEB_PATH        = 'https://irs.thsrc.com.tw/IMINT/'

# =========================================================================== #
#                                                                             #
#                                                                             #
# =========================================================================== #

def get_driver():
    global web_driver
    web_driver = webdriver.Chrome(CHROME_PATH)
    web_driver.get(WEB_PATH)
    web_driver.maximize_window()

    web_driver.find_element_by_id("btn-confirm").click()
    sleep(0.5)
    web_driver.find_element_by_xpath('//*[@id="goEN"]').click()
    
    
def get_captcha(index):
    # screenshot and find out the location of the captcha    
    web_driver.save_screenshot(OUTPUT_PATH + '/img_source{0:04}.png'.format(index)) 
    element = web_driver.find_element_by_id('BookingS1Form_homeCaptcha_passCode')
    
    if platform.system() == 'Darwin':
        left   = element.location['x']*2 ; top    = element.location['y']*2
        right  = element.location['x']*2 + element.size['width']*2
        bottom = element.location['y']*2 + element.size['height']*2
    else:
        left   = element.location['x'] ; top    = element.location['y']
        right  = element.location['x'] + element.size['width']
        bottom = element.location['y'] + element.size['height']
    
    img  = Image.open(OUTPUT_PATH + '/img_source{0:04}.png'.format(index))
    img2 = img.crop((left,top,right,bottom))
    img2.save(OUTPUT_PATH + '/img_source{0:04}.png'.format(index))

# =========================================================================== #
#                                                                             #
#                                                                             #
# =========================================================================== #    
    
if __name__ == '__main__':
   
    get_driver()
    
    for index in range(10):
        get_captcha(index)
