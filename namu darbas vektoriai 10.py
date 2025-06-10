import os
from dotenv import load_dotenv
from openai import OpenAI

text = ["How can I create"]

load_dotenv()
token = os.getenv("GITHUB_TOKEN")

print(token)

endpoint = "https://models.github.ai/inference"
model = "text-embedding-3-small"