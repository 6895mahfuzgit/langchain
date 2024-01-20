from langchain_openai import ChatOpenAI

llm_model = "gpt-4"  
chat = ChatOpenAI(temperature=0.0, model=llm_model)
