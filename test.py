import os
import httpx
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

client = httpx.Client(verify=False)

llm = ChatOpenAI(
    base_url=os.getenv("BASE_URL"),
    model="azure_ai/genailab-maas-DeepSeek-V3-0324",
    api_key=os.getenv("API_KEY"),
    http_client=client,
)

response = llm.invoke("Hi")
print(response.content)
