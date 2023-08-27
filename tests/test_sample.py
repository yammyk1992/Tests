import pytest as pt

from my_test_func.utils import func


@pt.mark.parametrize("a, b, expected_result", [(6, 3, 2),
                                               (9, 3, 3),
                                               (99, 33, 3)])
def test_answer_good(a, b, expected_result):
    assert func(a, b) == expected_result


@pt.mark.parametrize("expected_exeption, divider, value", [(ZeroDivisionError, 0, 10),
                                                           (TypeError, "2", 20)])
def test_answer_error(expected_exeption, divider, value):
    with pt.raises(expected_exeption):
        func(value, divider)
