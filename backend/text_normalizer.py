import re


def normalize_ocr_text(text: str) -> str:
    """
    Basic normalization for noisy OCR text.

    This function does not identify the medicine.
    It only cleans common OCR formatting errors.
    """

    if not text:
        return ""

    text = text.strip()

    # Normalize whitespace
    text = re.sub(r"\s+", " ", text)

    # Common OCR substitutions around dosage/strength
    text = re.sub(r"\bC(\d+)\)", r"\1", text)

    # Normalize common dosage units
    text = re.sub(r"\bU0\b", "40", text, flags=re.IGNORECASE)

    # Normalize common frequency OCR errors
    text = re.sub(r"\bODB\b", "OD", text, flags=re.IGNORECASE)
    text = re.sub(r"\bBDA\b", "BID", text, flags=re.IGNORECASE)

    return text.strip()