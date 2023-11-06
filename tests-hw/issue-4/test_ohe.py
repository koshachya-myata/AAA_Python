"""OneHotEncoder fit_transform tests."""
import pytest
from one_hot_encoder import fit_transform


@pytest.mark.parametrize(
    "src_documents,result",
    [
        (
            ['Moscow', 'Saint Petersburg', 'Novosibirsk', 'Kazan', 'Moscow'],
            [
                ('Moscow', [0, 0, 0, 1]),
                ('Saint Petersburg', [0, 0, 1, 0]),
                ('Novosibirsk', [0, 1, 0, 0]),
                ('Kazan', [1, 0, 0, 0]),
                ('Moscow', [0, 0, 0, 1]),
            ]
        ),
        (
            ['buy', 'sell'],
            [('buy', [0, 1]), ('sell', [1, 0])]
        ),
        (
            ['cat'] * 10,
            [('cat', [1])] * 10
        ),
    ]
)
def test_fit_transform_basic_input(src_documents, result):
    """Test that basic inputs works."""
    assert fit_transform(src_documents) == result


def test_raise_type_error():
    """Test that TypeError raised if incorrect input."""
    with pytest.raises(TypeError):
        fit_transform(11)
    with pytest.raises(TypeError):
        fit_transform(None)


def test_multiargs():
    """Test that OHE fit_transform works with multiple argumnets."""
    args = ['arg1', 'arg2', 'arg3']
    exp_result = [
            ('arg1', [0, 0, 1]),
            ('arg2', [0, 1, 0]),
            ('arg3', [1, 0, 0]),
        ]
    result = fit_transform(*args)
    assert result == exp_result


def test_empty():
    """Test that OHE fit_transform works with empty string input."""
    result = fit_transform('')
    assert result == [('', [1])]
