# Solution to:
#
# Write fibbonaci iteratively and recursively (bonus: use dynamic programming)
# where the fibbonaci sequences goes as follows:
#
# 1, 1, 2, 3, 5, 8, ...

def fib_recursive(n):
    """
    Returns nth number in the fibonacci sequence assuming
    zero-indexing. Computed recursively.
    :param n: which number in the sequence you are interested in
    :return: The nth number in the fibonacci sequence
    >>> fib_recursive(1)
    1
    >>> fib_recursive(0)
    1
    >>> fib_recursive(2)
    2
    >>> fib_recursive(3)
    3
    >>> fib_recursive(4)
    5
    >>> fib_recursive(5)
    8
    """
    if n <= 1:
        return 1
    return fib_recursive(n-1) + fib_recursive(n-2)


def fib_iter(n):
    """
    Returns nth number in the fibonacci sequence assuming zero-indexing.
    Computed iteratively.
    :param n: which number in the sequence you are interested in
    :return: The nth number in the fibonacci sequence
    >>> fib_iter(1)
    1
    >>> fib_iter(0)
    1
    >>> fib_iter(2)
    2
    >>> fib_iter(3)
    3
    >>> fib_iter(4)
    5
    >>> fib_iter(5)
    8
    """

    pred, curr = 1, 1
    counter = 1
    while counter < n:
        pred, curr = curr, curr + pred
        counter += 1
    return curr


def fib_dp(n):
    """
    Returns the first n numbers in the fibonacci sequence, computed using
    dynamic programming
    :param n: the number of numbers you want
    :return: a list containing the first n numbers in the fibonacci sequence
    >>> fib_dp(1)
    [1]
    >>> fib_dp(2)
    [1, 1]
    >>> fib_dp(3)
    [1, 1, 2]
    >>> fib_dp(4)
    [1, 1, 2, 3]
    >>> fib_dp(5)
    [1, 1, 2, 3, 5]
    >>> fib_dp(6)
    [1, 1, 2, 3, 5, 8]
    """
    assert n > 0, "n must be greater than 0"
    if n == 1:
        return [1]

    sequence = [1] * n
    for i in range(2, len(sequence)):
        sequence[i] = sequence[i-1] + sequence[i-2]
    return sequence


