# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 13:56:25 2024

@author: MahfuzShazol
"""
import os
import keys
from langchain.llms import OpenAI

os.environ['OPENAI_API_KEY'] =keys.OPENAI_API_KEY
llm=OpenAI(temperature=0.6)

text = "Suggest a personalized workout routine for someone looking to improve cardiovascular endurance and prefers outdoor activities."

print(llm(text))
