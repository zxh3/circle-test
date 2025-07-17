from circle_test import add


def test_add() -> None:
    assert add(1, 2) == 3


def test_sub() -> None:
    assert sub(1, 3) == -2
