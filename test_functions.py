from main import count_char, check_if_maj, check_if_special, check_if_valid_password

def test_count_char():
    input = "Bonjour"
    expected = 7
    result = count_char(input)
    assert expected == result