def check_question_intent():

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
  else:
    print("\n❌ Intent: OFF-TOPIC")

# --- Run the function ---
if __name__ == "__main__" : 
  check_question_intent()