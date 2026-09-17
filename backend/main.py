from fastapi import FastAPI, UploadFile, File
from pathlib import Path
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

app = FastAPI(title="Medical Shop AI")

UPLOAD_DIR = Path("data/raw")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


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

    return {
        "message": "Prescription processed successfully",
        "filename": file.filename,
        "extracted_text": text
    }