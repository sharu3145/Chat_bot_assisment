# summarize_chunks.py
from generate import generate_answer

def summarize_chunks(chunks):
    """
    Summarizes each chunk into 1 ultra-concise sentence with only essential actionable medical info.
    Removes all unnecessary details, references, or background.
    """
    summarized_chunks = []
    for chunk in chunks:
        prompt = f"""
Chunk:
{chunk}

Summarize this into **1 very short sentence** containing only **essential actionable medical advice**.
- Do NOT include figures, references, page numbers, or extra background.
- Do NOT repeat information already obvious.
- Keep it extremely concise for end-user readability.
"""
        summary = generate_answer(chunk, prompt)
        summarized_chunks.append(summary)
    return summarized_chunks