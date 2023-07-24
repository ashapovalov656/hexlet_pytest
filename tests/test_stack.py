import pytest


def test_stack():
    stack = []
    stack.append("one")
    stack.append("two")

    assert stack.pop() == "two"
    assert stack.pop() == "one"


def test_stack_emptiness():
    stack = []
    assert not stack
    stack.append(1)
    assert stack

    stack.pop()
    assert not stack


def test_pop_with_empty_stack():
    stack = []
    with pytest.raises(IndexError):
        stack.pop()
