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

def test_parse_medicine_name_only():
    from backend.medicine_extractor import parse_medicine_line

    result = parse_medicine_line("Betaloc")

    assert result["medicine_name"] == "Betaloc"
    assert result["strength"] is None
    assert result["dose"] is None
    assert result["frequency"] is None
    assert result["quantity"] is None

def test_parse_medicine_with_tablet_prefix():
    from backend.medicine_extractor import parse_medicine_line

    result = parse_medicine_line("Tab Betaloc 100 mg")

    assert result["medicine_name"] == "Betaloc"
    assert result["strength"] == "100 mg"
    assert result["dose"] is None
    assert result["frequency"] is None

def test_parse_medicine_with_quantity():
    from backend.medicine_extractor import parse_medicine_line

    result = parse_medicine_line("Betaloc 100mg - 10 tablets")

    assert result["medicine_name"] == "Betaloc"
    assert result["strength"] == "100mg"
    assert result["quantity"] == "10 tablets"
    assert result["dose"] is None
    assert result["frequency"] is None

def test_parse_medicine_quantity_without_dash():
    from backend.medicine_extractor import parse_medicine_line

    result = parse_medicine_line("Betaloc 100mg 10 tablets")

    assert result["medicine_name"] == "Betaloc"
    assert result["strength"] == "100mg"
    assert result["quantity"] == "10 tablets"
    assert result["dose"] is None
    assert result["frequency"] is None