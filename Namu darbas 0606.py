import os
from dotenv import load_dotenv
from openai import OpenAI

#token = os.environ["GITHUB_TOKEN"]

load_dotenv()
token = os.getenv("GITHUB_TOKEN")

print(token)

endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"

user_question = input("Please enter your question: ")

  # ### 2. 🎯 Intent Check
  # Define the list of keywords.
KW = ["apartment", "flat", "room", "renovation", "furniture", "storage", "decor"]

  # Convert the input question to lowercase.
lowercase_question = user_question.lower()

  # Check if any keyword is present in the lowercase question.
  # The any() function returns True if any item in an iterable is true.
is_on_topic = any(keyword in lowercase_question for keyword in KW)

  # --- Output the result ---
if is_on_topic:
    print("\n✅ Intent: ON-TOPIC")
    client = OpenAI(
    base_url=endpoint,
    api_key=token,
    )
    response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are an expert on improving apartments."
        },
        {
            "role": "user",
            "content": user_question,
        }
    ],
    temperature=0.7,
    top_p=1.0,
    model=model
    )
    print(response.choices[0].message.content)
else:
    print("\n❌ Sorry, I don't have knowledge on that.")



