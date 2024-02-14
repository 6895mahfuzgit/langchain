# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 14:09:58 2024

@author: MahfuzShazol
"""

import os
import keys

from langchain.llms import OpenAI
from langchain.chains import ConversationChain 
from langchain.memory import ConversationBufferMemory


os.environ['OPENAI_API_KEY'] =keys.OPENAI_API_KEY
llm=OpenAI(temperature=0)

conversation=ConversationChain(llm=llm,
                               verbose=True,
                               memory=ConversationBufferMemory())

conversation.predict(input="Tell me about yourself.")

conversation.predict(input="What can you do?")
conversation.predict(input="How can you help me with data analysis?")

print(conversation)


