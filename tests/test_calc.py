import pytest

from app.calc import add


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (2, 3, 5),
        (-2, -3, -5),
        (-2, 3, 1),
        (0, 0, 0),
        (0, 7, 7),
        (7, 0, 7),
        (10**12, 10**12, 2 * 10**12),
        (-10**12, 10**12, 0),
        (-(2**31), (2**31) - 1, -1),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected
