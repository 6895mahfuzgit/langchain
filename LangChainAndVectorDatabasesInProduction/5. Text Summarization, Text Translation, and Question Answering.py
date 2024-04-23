# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 14:43:53 2024

@author: HP
"""
import os
import keys

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import DeepLake
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType 
from langchain import PromptTemplate

os.environ['OPENAI_API_KEY'] =keys.OPENAI_API_KEY
os.environ['ACTIVELOOP_TOKEN'] =keys.ACTIVELOOP_TOKEN

template = """Question: {question}

Answer: """
prompt = PromptTemplate(
    template=template,
    input_variables=['question']
)

# user question
question = "What is the capital city of France?"