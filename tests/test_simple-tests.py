import pytest
from inject_objects import inject_objects as inject


def test_inject():
    @inject(a=1, b=3)
    def foo():
        return a + b

    assert foo() == 4


def test_no_injcet():
    def foo():
        return a + b

    try:
        foo() == 4
        assert False
    except Exception:
        assert True


def test_with_args():
    @inject(a=1, b=2)
    def foo(x=3, y=4):
        return a * x + b * y

    assert foo() == 3 + 8


def test_with_args_fail():
    def foo(x=3, y=4):
        return a * x + b * y

    try:
        foo()
    except Exception:
        assert True
