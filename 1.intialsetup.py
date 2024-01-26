import os
from langchain.llms import OpenAI


os.environ['OPENAI_API_KEY'] =''
llm=OpenAI(temperature=0.6)
ans=llm("what is life")
print(ans)

