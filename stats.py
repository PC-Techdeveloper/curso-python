def mean(*values):
    """Calculate mean of values."""
    return sum(values) / len(values)


def std(*values):
    """Calculate standard deviation of values."""
    m = mean(*values)
    p = sum((value - m) ** 2 for value in values)
    return (p / (len(values) - 1)) ** (1 / 2)
