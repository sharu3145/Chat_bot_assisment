import pdfplumber

def extract_text(pdf_path):
    full_text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                full_text += text

    return full_text


if __name__ == "__main__":
    text = extract_text("data/medical.pdf")
    print(text[:1000])