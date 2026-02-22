from dotenv import load_dotenv
import os
from huggingface_hub import InferenceClient

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

print("DEBUG TOKEN:", HF_TOKEN)  # temporary debug

client = InferenceClient(
    model="HuggingFaceH4/zephyr-7b-beta",
    token=HF_TOKEN
)

def generate_answer(context, question):

    messages = [
        {
            "role": "system",
            "content": "You are a helpful medical assistant. Use ONLY the provided context to answer."
        },
        {
            "role": "user",
            "content": f"""
Context:
{context}

Question:
{question}

If the answer is not in the context, say:
'I don't know based on the provided information.'
"""
        }
    ]

    response = client.chat_completion(
        messages=messages,
        max_tokens=300,
        temperature=0.3,
    )

    return response.choices[0].message.content