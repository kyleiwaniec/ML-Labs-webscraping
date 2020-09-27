#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 00:13:49 2020

@author: Long Mai
"""

# =========================================================================== #
#                                                                             #
#                                                                             #
# =========================================================================== #

WEB_PATH    = 'http://encheng-chang.at.tw/ForTest/test/user_agent.php'
ACCT        = 'ml-lab'
PD          = 'ucdcs'

# =========================================================================== #
#                                                                             #
#                                                                             #
# =========================================================================== #    

from requests.auth import HTTPBasicAuth
import requests

if __name__ == '__main__':
    
    article = requests.get(WEB_PATH, auth=HTTPBasicAuth(ACCT, PD)).text
    print(article)