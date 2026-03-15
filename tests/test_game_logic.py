from logic_utils import check_guess
from app import parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == ("Too High", "📉 Go LOWER!")

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")

def test_parse_guess_valid_integer():
    assert parse_guess("42") == (True, 42, None)

def test_parse_guess_valid_float():
    assert parse_guess("42.0") == (True, 42, None)

def test_parse_guess_invalid_string():
    assert parse_guess("abc") == (False, None, "That is not a number.")

def test_parse_guess_empty_string():
    assert parse_guess("") == (False, None, "Enter a guess.")

def test_parse_guess_none():
    assert parse_guess(None) == (False, None, "Enter a guess.")
