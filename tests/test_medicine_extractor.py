from backend.medicine_extractor import extract_medicine_lines


def test_extract_medicine_lines():
    text = """
    MEDICAL CENTRE
    John Smith
    162 Example Street

    Betaloc 100mg - 1 tab BID
    Dorzolamide 10 mg - 1 tab BID
    Cimetidine 50 mg - 2 tabs TID

    Dr. Steve Johnson
    Signature
    """

    result = extract_medicine_lines(text)

    assert "Betaloc 100mg - 1 tab BID" in result
    assert "Dorzolamide 10 mg - 1 tab BID" in result
    assert "Cimetidine 50 mg - 2 tabs TID" in result

    assert "John Smith" not in result
    assert "Dr. Steve Johnson" not in result

def test_parse_medicine_line():
    from backend.medicine_extractor import parse_medicine_line

    result = parse_medicine_line(
        "Betaloc 100mg - 1 tab BID"
    )

    assert result["medicine_name"] == "Betaloc"
    assert result["strength"] == "100mg"
    assert result["dose"] == "1 tab"
    assert result["frequency"] == "BID"    