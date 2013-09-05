"""
examples/assert/euler01.py
Project Euler, problem 1

"""
def multiples35(upper_limit):
    # TODO: This is *not* the real answer
    if upper_limit == 10:
        return [3, 5, 6, 9]
    return []


def test_known_inputs():
    # Check known outputs
    assert multiples35(10) == [3, 5, 6, 9]
    assert sum(multiples35(10)) == 23


def test_solution():
    assert sum(multiples35(1000)) != 0
    # TODO: Get real answer
    print(sum(multiples35(1000)))
