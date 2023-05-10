"""
Queue to stack converter.
"""


from arrayqueue import ArrayQueue
from arraystack import ArrayStack


def queue_to_stack(queue: ArrayQueue):
    """
    Convert a queue to a stack.
    >>> queue = ArrayQueue()
    >>> queue.add(0)
    >>> queue.add(1)
    >>> queue.add(2)
    >>> queue.add(3)
    >>> queue.add(4)
    >>> queue.add(5)
    >>> queue.add(6)
    >>> queue.add(7)
    >>> queue.add(8)
    >>> queue.add(9)
    >>> stack = queue_to_stack(queue)
    >>> print(queue)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> print(stack)
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    >>> print(stack.pop())
    0
    >>> print(queue.pop())
    0
    >>> stack.add(11)
    >>> queue.add(11)
    >>> print(queue)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
    >>> print(stack)
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 11]
    """
    stack = ArrayStack()
    temporary_stack = ArrayStack()
    temporary_queue = ArrayQueue()

    while queue.isEmpty() is not True:
        zminna = queue.pop()
        temporary_stack.push(zminna)
        temporary_queue.add(zminna)

    while temporary_queue.isEmpty() is not True:
        zminna = temporary_queue.pop()
        queue.add(zminna)

    while temporary_stack.isEmpty() is not True:
        zminna = temporary_stack.pop()
        stack.push(zminna)

    return stack


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
