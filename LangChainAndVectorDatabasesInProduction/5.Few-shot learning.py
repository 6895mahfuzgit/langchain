# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 16:05:24 2024

@author: Mahfuzur_Shazol
"""
from langchain import PromptTemplate
from langchain import FewShotPromptTemplate

# create our examples
examples = [
    {
        "query": "What's the weather like?",
        "answer": "It's raining cats and dogs, better bring an umbrella!"
    }, {
        "query": "How old are you?",
        "answer": "Age is just a number, but I'm timeless."
    }
]

  # create an example template      
example_template = """
User: {query}
AI: {answer}
"""
