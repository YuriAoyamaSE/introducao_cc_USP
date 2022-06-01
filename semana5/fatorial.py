def fatorial(n: int) -> int:
    fat = 1
    while n > 1:
        fat *= n
        n -=1
    return fat


def test_fatorial():
    assert fatorial(2) == 1
    