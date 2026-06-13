from docling.document_converter import DocumentConverter

def main():
    converter = DocumentConverter()
    result = converter.convert("sanchitx1-resume.pdf")
    text = result.document.export_to_text()
    chunk_size = 1000
    overlap = 200
    chunks = []
    
    for i in range(0, len(text), chunk_size - overlap):
        chunks.append(text[i:i + chunk_size])
    
    print(f"Created {len(chunks)} chunks\n")
    
    for idx, chunk in enumerate(chunks, start=1):
        print(f"--- CHUNK {idx} ---")
        print(chunk)
        print("\n")

if __name__ == "__main__":
    main()
