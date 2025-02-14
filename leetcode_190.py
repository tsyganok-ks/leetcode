def reverseBits(n):
    """
    Reverse bits of a given 32 bits unsigned integer
    :param n: bits
    :return: int number of reversed bits
    """
    return int('0b' + bin(n + 2 ** 32)[:2:-1], 2)