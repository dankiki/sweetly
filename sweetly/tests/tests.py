import sweetly.helpers as helpers


def test_int_to_base64():
    """Check that int_to_base64 generates 1M short base64 combinations
    and there are no clashes"""
    max_value = 1000000
    encoded = [helpers.int_to_base64(num) for num in range(0, max_value)]
    encoded_set = set(encoded)
    assert len(encoded) == len(encoded_set)
