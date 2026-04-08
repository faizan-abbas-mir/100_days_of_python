import os
import sys
from dotenv import load_dotenv
load_dotenv()


ai_url="http//openai.api.v1."
model_id='gpt-4.o-mini'
api_key=os.getenv("open_ai_key")
print(api_key)
