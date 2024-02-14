# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 14:02:30 2024

@author: HP
"""
import os
import keys

from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain


os.environ['OPENAI_API_KEY'] =keys.OPENAI_API_KEY
llm=OpenAI(temperature=0.6)

prompt=PromptTemplate(input_variables=["product"],
                      
                      template="What is a good name for a company that makes {product}?")



chain=LLMChain(llm=llm,prompt=prompt)

print(chain.invoke("eco-friendly water bottles"))


