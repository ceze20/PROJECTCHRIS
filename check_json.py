import json

input_path = r"C:\Users\ezet4\OneDrive\Desktop\PythonApI\pdf_text.json"

with open(input_path, "r", encoding="utf-8") as f:
    data = json.load(f)

print(data[:2])  # Print first 2 pages
