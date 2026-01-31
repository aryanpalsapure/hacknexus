import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("AIzaSyDgJAQFAyzFJIdw-OTnjwa7g7Md9y7czUU"))

print("\nAVAILABLE MODELS:\n")

for m in client.models.list():
    print(m)
