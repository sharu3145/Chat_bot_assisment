# final_answer.py
from generate import generate_answer

def answer_from_summaries(summaries, question):
    """
    Generate final answer using summarized chunks.
    Ensures answer is short, clean, and actionable.
    """
    context = "\n".join(summaries)
    prompt = f"""
Context:
{context}

Question:
{question}

Using only this context, provide a concise answer in **3-4 sentences max**.
- Include actionable advice only.
- Do NOT copy context verbatim.
- Remove any unnecessary details, figures, or references.
- If the answer is not in the context, say: 'I don't know based on the provided information.'
"""
    return generate_answer(context, prompt)