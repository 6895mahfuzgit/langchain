# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 15:40:10 2024

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
 

os.environ['OPENAI_API_KEY'] =keys.OPENAI_API_KEY
os.environ['ACTIVELOOP_TOKEN'] =keys.ACTIVELOOP_TOKEN

llm = OpenAI(temperature=0)
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

texts = [
    "Mahfuz Born in Dhaka in 4 January 1994."
   # "Napoleon Bonaparte was born in 15 August 1769",
    #"Louis XIV was born in 5 September 1638"
]

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.create_documents(texts)

my_activeloop_org_id =keys.ACTIVELOOP_ORG_ID  
my_activeloop_dataset_name = keys.ACTIVELOOP_DATASET_NAME
dataset_path = keys.ACTIVELOOP_DATASET_PATH
db = DeepLake(dataset_path=dataset_path, embedding_function=embeddings)

# add documents to our Deep Lake dataset
#db.add_documents(docs)

retrieval_qa = RetrievalQA.from_chain_type(
	llm=llm,
	chain_type="stuff",
	retriever=db.as_retriever()
)


tools = [
    Tool(
        name="Retrieval QA System",
        func=retrieval_qa.run,
        description="Useful for answering questions."
    ),
]

agent = initialize_agent(
	tools,
	llm,
	agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
	verbose=True
)

response = agent.run("When was Mahfuz born?")
print(response)


