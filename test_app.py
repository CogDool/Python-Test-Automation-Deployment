from app import calculate_total

def test_calculate_total():
    # Tests if $100 + 10% tax correctly equals $110
    assert calculate_total(100.0, 0.10) == 110.0

