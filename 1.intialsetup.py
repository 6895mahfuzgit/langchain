import os
from langchain.llms import OpenAI
import keys

os.environ['OPENAI_API_KEY'] =keys.OPENAI_API_KEY
llm=OpenAI(temperature=0.6)
ans=llm("what is life")
print(ans)

