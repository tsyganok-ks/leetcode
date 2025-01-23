def smallestEvenMultiple(n):
    """Return the smallest positive integer that is a multiple of both 2 and n"""
    return n * 2 if (n / 2) % 1 > 0 else n