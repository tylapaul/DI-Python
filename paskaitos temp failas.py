#naujas failas
import os
from dotenv import load_dotenv

load_dotenv()
secret = os.getenv("GITHUB_TOKEN")

print(secret)