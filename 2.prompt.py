import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


os.environ['OPENAI_API_KEY'] =''

llm=OpenAI(temperature=0.6)

prompt_template_name= PromptTemplate( input_variables=['cusine'],template="I want to open a restuarent for {cusine} food.Suggest a nice name for this.")
#prompt_template_name.format(cusine="Bangladesh")

chain=LLMChain(llm=llm,prompt=prompt_template_name)
result=chain.run("Bangladesh")

print(result)

