import re


def extract_medicine_lines(text: str):
    lines = text.splitlines()

    medicine_lines = []

    for line in lines:
        clean_line = line.strip()

        if not clean_line:
            continue

        has_strength = re.search(
            r"\b\d+\s?(mg|ml|mcg|g)\b",
            clean_line,
            re.IGNORECASE
        )

        has_dosage_keyword = re.search(
            r"\b(tab|tablet|cap|capsule|bid|tid|qd|od|bd|sos)\b",
            clean_line,
            re.IGNORECASE
        )

        if has_strength or has_dosage_keyword:
            medicine_lines.append(clean_line)

    return medicine_lines


def parse_medicine_line(line: str):
    line = line.strip()

    if not line:
        return None

    # Format 1:
    # Betaloc 100mg - 1 tab BID
    full_pattern = (
        r"^(?:tab|tablet|cap|capsule)?\s*"
        r"(.+?)\s+"
        r"(\d+\s?(?:mg|ml|mcg|g))"
        r"\s*-\s*"
        r"(.+?)\s+"
        r"(BID|TID|QD|OD|BD|SOS)$"
    )

    match = re.search(full_pattern, line, re.IGNORECASE)

    if match:
        medicine_name = match.group(1).strip()
        strength = match.group(2).strip()
        dose = match.group(3).strip()
        frequency = match.group(4).strip().upper()

        return {
            "medicine_name": medicine_name,
            "strength": strength,
            "dose": dose,
            "frequency": frequency,
            "quantity": None,
            "raw_text": line
        }

    # Format 1B:
    # Betaloc 100mg - 10 tablets
    quantity_pattern = (
        r"^(.+?)\s+"
        r"(\d+\s?(?:mg|ml|mcg|g))"
        r"\s*-\s*"
        r"(\d+\s+(?:tablet|tablets|tab|tabs|capsule|capsules|cap|caps))$"
    )

    match = re.search(
        quantity_pattern,
        line,
        re.IGNORECASE
    )

    if match:
        medicine_name = match.group(1).strip()
        strength = match.group(2).strip()
        quantity = match.group(3).strip()

        return {
            "medicine_name": medicine_name,
            "strength": strength,
            "dose": None,
            "frequency": None,
            "quantity": quantity,
            "raw_text": line
        }

    # Format 2:
    # Tab Betaloc 100 mg
    strength_with_prefix_pattern = (
        r"^(?:tab|tablet|cap|capsule)\s+"
        r"(.+?)\s+"
        r"(\d+\s?(?:mg|ml|mcg|g))$"
    )

    match = re.search(
        strength_with_prefix_pattern,
        line,
        re.IGNORECASE
    )

    if match:
        medicine_name = match.group(1).strip()
        strength = match.group(2).strip()

        return {
            "medicine_name": medicine_name,
            "strength": strength,
            "dose": None,
            "frequency": None,
            "quantity": None,
            "raw_text": line
        }
        # Format 1C:
    # Betaloc 100mg 10 tablets
    quantity_no_dash_pattern = (
        r"^(.+?)\s+"
        r"(\d+\s?(?:mg|ml|mcg|g))\s+"
        r"(\d+\s+(?:tablet|tablets|tab|tabs|capsule|capsules|cap|caps))$"
    )

    match = re.search(
        quantity_no_dash_pattern,
        line,
        re.IGNORECASE
    )

    if match:
        medicine_name = match.group(1).strip()
        strength = match.group(2).strip()
        quantity = match.group(3).strip()

        return {
            "medicine_name": medicine_name,
            "strength": strength,
            "dose": None,
            "frequency": None,
            "quantity": quantity,
            "raw_text": line
        }

    # Format 3:
    # Betaloc 100 mg
    strength_only_pattern = (
        r"^(.+?)\s+"
        r"(\d+\s?(?:mg|ml|mcg|g))$"
    )

    match = re.search(
        strength_only_pattern,
        line,
        re.IGNORECASE
    )

    if match:
        medicine_name = match.group(1).strip()
        strength = match.group(2).strip()

        return {
            "medicine_name": medicine_name,
            "strength": strength,
            "dose": None,
            "frequency": None,
            "quantity": None,
            "raw_text": line
        }

    # Format 4:
    # Betaloc
    return {
        "medicine_name": line,
        "strength": None,
        "dose": None,
        "frequency": None,
        "quantity": None,
        "raw_text": line
    }