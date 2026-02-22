# generate.py
from dotenv import load_dotenv
import os
from huggingface_hub import InferenceClient

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

client = InferenceClient(
    model="HuggingFaceH4/zephyr-7b-beta",
    token=HF_TOKEN
)

# System prompt for concise, human-friendly medical answers
system_prompt = """
You are a friendly and helpful medical assistant.
- Answer the user’s question naturally and concisely.
- Use the context only as reference; do NOT copy chunks verbatim.
- Include only the most relevant information.
- Provide actionable advice if applicable.
- Keep answers short (3-4 sentences max).
- If the answer is not in the context, say: 'I don't know based on the provided information.'
"""

def generate_answer(context, question):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Context:\n{context}\n\nQuestion:\n{question}"}
    ]

    response = client.chat_completion(
        messages=messages,
        max_tokens=300,
        temperature=0.3,
    )

    return response.choices[0].message.content