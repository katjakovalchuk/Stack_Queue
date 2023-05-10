"""
Stack to queue converter.
"""

from arrayqueue import ArrayQueue
from arraystack import ArrayStack


def stack_to_queue(stack):
    """
    Convert a stack to a queue.
    >>> stack = ArrayStack()
    >>> stack.add(0)
    >>> stack.add(1)
    >>> stack.add(2)
    >>> stack.add(3)
    >>> stack.add(4)
    >>> stack.add(5)
    >>> stack.add(6)
    >>> stack.add(7)
    >>> stack.add(8)
    >>> stack.add(9)
    >>> queue = stack_to_queue(stack)
    >>> print(queue)
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    >>> print(stack)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> print(stack.pop())
    9
    >>> print(queue.pop())
    9
    >>> stack.add(11)
    >>> queue.add(11)
    >>> print(queue)
    [8, 7, 6, 5, 4, 3, 2, 1, 0, 11]
    >>> print(stack)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 11]
    """
    queue = ArrayQueue()
    temporary_stack = ArrayStack()
    temporary_queue = ArrayQueue()

    while stack.isEmpty() is not True:
        zminna = stack.pop()
        temporary_stack.push(zminna)
        temporary_queue.add(zminna)

    while temporary_queue.isEmpty() is not True:
        zminna = temporary_queue.pop()
        queue.add(zminna)

        while temporary_stack.isEmpty() is not True:
            zminna = temporary_stack.pop()
            stack.push(zminna)

    return queue


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
