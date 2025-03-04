import json

input_path = r"C:\Users\ezet4\OneDrive\Desktop\PythonApI\pdf_text_improved.json"

# Load the extracted text
with open(input_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Print the first 2 extracted pages
print("\n🔍 First 2 pages of extracted text:\n")
for page in data[:2]:
    print(f"📄 Page {page['page']}:\n{page['text'][:1000]}...\n")  # Print first 1000 characters
