def chunk_text(text, chunk_size=800, overlap=100):
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size

        chunk = text[start:end]
        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


if __name__ == "__main__":
    from extract_text import extract_text

    text = extract_text("data/medical.pdf")
    chunks = chunk_text(text)

    print("Total chunks:", len(chunks))
    print("\nSample chunk:\n")
    print(chunks[0][:500])