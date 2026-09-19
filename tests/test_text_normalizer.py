from backend.text_normalizer import normalize_ocr_text


def test_normalize_frequency():
    assert normalize_ocr_text("Aceclofenac C100) BDA") == \
        "Aceclofenac 100 BID"


def test_normalize_od():
    assert normalize_ocr_text("Pantoprazole C40) ODB") == \
        "Pantoprazole 40 OD"


def test_normalize_empty_text():
    assert normalize_ocr_text("") == ""