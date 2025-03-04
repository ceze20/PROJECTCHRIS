import fitz  # PyMuPDF
import json
import pytesseract  # OCR
from PIL import Image
import io

# Set up Tesseract (for OCR if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text_from_pdf(pdf_path):
    text_data = []
    doc = fitz.open(pdf_path)

    for page_num in range(len(doc)):
        text = doc[page_num].get_text("text")

        # If no text is found, try OCR (image recognition)
        if not text.strip():
            img_list = doc[page_num].get_images(full=True)
            if img_list:
                text = ""
                for img_index, img in enumerate(img_list):
                    xref = img[0]
                    base_image = doc.extract_image(xref)
                    image_data = base_image["image"]
                    img = Image.open(io.BytesIO(image_data))
                    ocr_text = pytesseract.image_to_string(img)
                    text += f"\n[OCR Extracted Text from Image {img_index + 1}]:\n{ocr_text}\n"

        # Remove unnecessary characters (e.g., "\x02", "\n")
        text = text.replace("\x02", "").strip()
        
        text_data.append({"page": page_num + 1, "text": text})

    return text_data

pdf_path = r"C:\Users\ezet4\OneDrive\Desktop\PythonApI\my_textbook.pdf"
output_path = r"C:\Users\ezet4\OneDrive\Desktop\PythonApI\pdf_text_improved.json"

pdf_text = extract_text_from_pdf(pdf_path)

# Save cleaned extracted text
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(pdf_text, f, indent=4)

print(f"✅ Improved text extraction completed! Results saved in {output_path}.")
