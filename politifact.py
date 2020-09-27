# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 00:08:41 2020

@author: en-chengchang
"""

# =========================================================================== #
#                                                                             #
#                                                                             #
# =========================================================================== #

from selenium import webdriver
import pandas as pd

# =========================================================================== #
#                                                                             #
#                                                                             #
# =========================================================================== #

CHROME_PATH = '/Users/en-chengchang/Downloads/chromedriver'
WEB_PATH = 'https://www.politifact.com/personalities/donald-trump/'

# =========================================================================== #
#                                                                             #
#                                                                             #
# =========================================================================== #

class scrape:
    
    def __init__(self, chrome_path = CHROME_PATH, maximise = True):
        self.driver = webdriver.Chrome(chrome_path)
        if maximise == True: self.driver.maximize_window()
            
    def get_access(self, web_path = WEB_PATH):
        self.driver.get(web_path)
    
    def get_element(self, xpath_pattern, index):
        element = self.driver.find_element_by_xpath(xpath_pattern.format(index))
        return element
    
    def get_element_text(self, xpath_pattern, index):
        return self.get_element(xpath_pattern, index).text
    
    def find_button(self, xpath):
        try:
            button = self.driver.find_element_by_xpath(xpath)
            return button
        except:
            return False
        
# =========================================================================== #
#                                                                             #
#                                                                             #
# =========================================================================== #
    
if __name__ == '__main__':
    
    web_driver = scrape()
    web_driver.get_access()
    
    button_load_more = web_driver.find_button('//*[@id="top"]/main/section[5]/div/div/a')
    if button_load_more: button_load_more.click()
    
    common_string = '//*[@id="top"]/main/section[3]/article/section/div/article/ul/li'
    content_pattern = common_string + '[{0}]/article/div[2]/div/div[1]/div'
    time_pattern    = common_string + '[{0}]/article/div[1]/div[2]/div'
    footer_pattern  = common_string + '[{0}]/article/div[2]/div/footer'
    truth_pattern   = common_string + '[{0}]/article/div[2]/div/div[2]/div/picture/img'
    
    button_next_xpath     = '//*[@id="top"]/main/section[4]/div/ul/li/a'
    button_previous_xpath = '//*[@id="top"]/main/section[4]/div/ul/li/a'
    element_index = 1
    data = {}
    
    while True:
        try:
            content = web_driver.get_element_text(content_pattern, element_index)
            time    = web_driver.get_element_text(time_pattern, element_index)
            footer  = web_driver.get_element_text(footer_pattern, element_index)
            truth   = web_driver.get_element(truth_pattern, element_index).get_attribute('alt')

            if content in data.keys(): 
                break
            else:
                data[content] = [time, content, footer, truth]
                element_index += 1
        except:
            if web_driver.find_button(button_next_xpath):
                web_driver.find_button(button_next_xpath).click()
                element_index = 1
            else: 
                break
        
    columns = ['time', 'content', 'footer', 'truth']
    dataset = pd.DataFrame([data[keys] for keys in data.keys()], columns = columns)
    dataset.to_csv('./data_selenium_politifact.csv', index = False)
    
        
            
            

