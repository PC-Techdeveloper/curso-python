def gcd(a, b):
    """Greatest common divisor through euclidean algorithm."""
    while b > 0:
        a, b = b, a % b
        return a


def lcm(a, b):
    """Least common multiple through euclidean algorithm."""
    return a * b // gcd(a, b)
