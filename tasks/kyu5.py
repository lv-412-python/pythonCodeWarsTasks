"""Implementation of Fibonacci function and Fibonacci product function."""


def fib(num):
    """
    Finds n-th element from a Fibonacci sequence.
    :param num: int : sequence number.
    :return: int : n-th element from a Fibonacci sequence.
    """
    first, second = 0, 1
    for _ in range(2, num - 1):
        first, second = second, first + second
    return second


def fib_product(product):
    """
    Finds two consistent Fibonacci numbers, being given their possible product.
    In case it is - returns a list with [fib(n), fib(n+1), True],
    otherwise [fib(n), fib(n+1), False].
    :param product: int : product of two numbers.
    :return: list : list with first two elements from Fibonacci sequence and a boolean.
    """
    current_value, num = 0, 0
    fib1 = fib2 = 0

    while current_value < product:
        num += 1
        fib1 = fib(num)
        fib2 = fib(num + 1)
        current_value = fib1 * fib2

    if current_value == product:
        return [fib1, fib2, True]

    return [fib1, fib2, False]
