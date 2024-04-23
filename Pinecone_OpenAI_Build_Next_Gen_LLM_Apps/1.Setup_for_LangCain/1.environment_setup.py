# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 16:59:49 2024

@author: HP
"""

import os
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv(),override=True)

print(os.environ.get('PINECON_API_KEY'))