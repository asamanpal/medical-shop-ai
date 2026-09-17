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
    pattern = r"^(.+?)\s+(\d+\s?(?:mg|ml|mcg|g))\s*-\s*(.+?)\s+(BID|TID|QD|OD|BD|SOS)$"

    match = re.search(pattern, line, re.IGNORECASE)

    if not match:
        return None

    medicine_name = match.group(1).strip()
    strength = match.group(2).strip()
    dose = match.group(3).strip()
    frequency = match.group(4).strip().upper()

    return {
        "medicine_name": medicine_name,
        "strength": strength,
        "dose": dose,
        "frequency": frequency
    }
