from langchain_openai import ChatOpenAI  
import os  
import httpx  
client = httpx.Client(verify=False) 
llm = ChatOpenAI( 
    base_url="https://genailab.tcs.in",
    model = "azure_ai/genailab-maas-DeepSeek-V3-0324", 
    api_key="sk-uoDXudpMggVIu9LSwZF1eQ", # Will be provided during event.  And this key is for 
    http_client = client 
) 
output = llm.invoke("Hi")
print(output)