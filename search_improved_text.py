import json

def search_pdf(query, text_chunks):
    results = []
    for chunk in text_chunks:
        if query.lower() in chunk["text"].lower():
            results.append(chunk)
    return results

# Load chunked text
input_path = r"C:\Users\ezet4\OneDrive\Desktop\PythonApI\pdf_text_improved.json"

with open(input_path, "r", encoding="utf-8") as f:
    text_chunks = json.load(f)

query = input("🔎 Enter your search query: ")
matches = search_pdf(query, text_chunks)

if matches:
    print("\n✅ Search Results:")
    for match in matches[:3]:  # Show only top 3 results
        print(f"\n📄 Page {match['page']}:\n{match['text'][:500]}...\n")  # Print first 500 characters
else:
    print("\n❌ No matching results found.")
