def series_sum(nth_num):
    """
    Calculates the sum of the series upto nth term

    Args:
        nth_num (int): nth term of the series
    Returns:
        str: The return value
    """
    if nth_num == 0:
        return format(0, '.2f')
    series = 1
    divisor = 4
    for i in range(0, nth_num - 1):
        series += 1 / divisor
        divisor += 3
    return format(series, '.2f')
