"""Decode test using pytest."""
from decode import decode
import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ('... --- ...', 'SOS'),
        (' '.join(['.-'] * 30), 'A' * 30),
        ('----- ..--..', '0?'),
        ('.... . .-.. .-.. --- --..-- .-- --- .-. .-.. -..', 'HELLO, WORLD')
    ]
)
def test_decode(test_input, expected):
    """Test morse decode."""
    assert decode(test_input) == expected
