from fastapi import FastAPI, Query
import json

app = FastAPI()

# Load extracted PDF text
import os

# Get the path relative to the app directory
input_path = os.path.join(os.path.dirname(__file__), "pdf_text_improved.json")


with open(input_path, "r", encoding="utf-8") as f:
    text_chunks = json.load(f)

def search_pdf(query: str):
    """Search for a query in the extracted PDF text."""
    results = []
    for chunk in text_chunks:
        if query.lower() in chunk["text"].lower():
            results.append({"page": chunk["page"], "text": chunk["text"][:500]})  # Return first 500 characters
    return results[:3]  # Limit results to top 3

@app.get("/")
def home():
    return {"message": "Welcome to the PDF Search API!"}

@app.get("/search")
def search(query: str = Query(..., description="Enter search keyword")):
    results = search_pdf(query)
    if results:
        return {"status": "success", "results": results}
    return {"status": "no results", "message": "No matching content found."}

