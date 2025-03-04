import os
import fitz  # PyMuPDF
import json

pdf_path = r"C:\Users\ezet4\OneDrive\Desktop\PythonApI\my_textbook.pdf"

# Check if the file exists before proceeding
if not os.path.exists(pdf_path):
    print(f"Error: File '{pdf_path}' does not exist. Check the file name and path.")
    exit()

def extract_text_from_pdf(pdf_path):
    text_data = []
    doc = fitz.open(pdf_path)

    for page_num in range(len(doc)):
        text = doc[page_num].get_text("text")
        text_data.append({"page": page_num + 1, "text": text})
    
    return text_data

pdf_text = extract_text_from_pdf(pdf_path)

# Save extracted text
output_path = r"C:\Users\ezet4\OneDrive\Desktop\PythonApI\pdf_text.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(pdf_text, f, indent=4)

print(f"Text extraction completed! Results saved in {output_path}.")
