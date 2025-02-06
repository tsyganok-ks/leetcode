def trailingZeroes(n):
    """
    Count the number of trailing zeroes in n!
    :param n: num
    :return: number of trailing zeroes
    """

    #n//5 + n//25 + n//125 + ... n//5**i

    return sum([n//(5**i)  for i in range(1, 10)])


def main():
    n = 1
    print(trailingZeroes(n))


if __name__ == '__main()':
    main()