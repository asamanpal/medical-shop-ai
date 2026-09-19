from fastapi import FastAPI, UploadFile, File
from pathlib import Path
import cv2
import pytesseract
from backend.medicine_search import search_medicines

from backend.medicine_extractor import (
    extract_medicine_lines,
    parse_medicine_line
)


app = FastAPI(title="Medical Shop AI")

UPLOAD_DIR = Path("data/raw")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


@app.get("/")
def home():
    return {
        "message": "Medical Shop AI backend is running 🚀"
    }


@app.post("/upload-prescription")
async def upload_prescription(file: UploadFile = File(...)):
    file_path = UPLOAD_DIR / file.filename

    contents = await file.read()
    file_path.write_bytes(contents)

    image = cv2.imread(str(file_path))

    if image is None:
        return {
            "message": "Could not read the uploaded image"
        }

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray)

    medicine_lines = extract_medicine_lines(text)

    medicines = []

    for line in medicine_lines:
        parsed = parse_medicine_line(line)

        if parsed:
            query = parsed["medicine_name"]

            if parsed["strength"]:
                query = f"{query} {parsed['strength']}"

            matches = search_medicines(query)

            parsed["matches"] = matches

            medicines.append(parsed)

    return {
        "message": "Prescription processed successfully",
        "filename": file.filename,
        "extracted_text": text,
        "medicine_lines": medicine_lines,
        "medicines": medicines
    }