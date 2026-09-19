from backend.medicine_search import search_medicines


def test_search_medicine_by_name():
    results = search_medicines("Betaloc")

    assert len(results) > 0
    assert any(
        "Betaloc" in medicine["name"]
        for medicine in results
    )


def test_search_medicine_by_name_and_strength():
    results = search_medicines("Betaloc 100mg")

    assert len(results) > 0
    assert any(
        "Betaloc 100mg" in medicine["name"]
        for medicine in results
    )


def test_unknown_medicine_returns_empty():
    results = search_medicines("MedicineThatDoesNotExist123")

    assert results == []