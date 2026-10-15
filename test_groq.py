import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": "Say hello in one short sentence."
        }
    ],
    max_tokens=50
)

print("Finish reason:", response.choices[0].finish_reason)
print("Message object:", response.choices[0].message)
print("Content:", repr(response.choices[0].message.content))