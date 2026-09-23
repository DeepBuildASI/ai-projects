import os
from groq import Groq

# Paste your Groq key here (between the quotes)
GROQ_API_KEY = "YOUR_GROQ_API_KEY"

client = Groq(api_key="YOUR_GROQ_API_KEY")

# Fake review for now (Google data comes later)
review = "The dentist was rude and the wait was 2 hours. Never coming back."

prompt = f"""You are the owner of a dental clinic. 
Write a short, polite, professional reply to this patient review.
Keep it under 3 sentences.

Review: {review}
"""

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[{"role": "user", "content": prompt}]
)

print("REVIEW:", review)
print()
print("REPLY:", response.choices[0].message.content)