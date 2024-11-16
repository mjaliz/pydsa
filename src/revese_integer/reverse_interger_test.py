import pytest
from .reverse_integer import reverse_int


@pytest.mark.parametrize(
    "number, expected",
    [
        (10, 1),
        (12, 21),
        (-87, -78),
        (-90, -9),
        (100, 1),
        (154, 451),
        (897, 798),
        (120, 21),
    ],
)
def test_reverse_int(number, expected):
    assert reverse_int(number) == expected
