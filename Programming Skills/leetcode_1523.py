def countOdds(low, high):
    """
    Count of odd numbers between low and high (inclusive)
    :param low: start num
    :param high: end num
    :return: count of odd
    """
    difference = high - low + 1
    if difference % 2 == 0:  # 2, 3, 4, 5, 6, 7, 8 , 9
        return difference // 2  # one of (low or high) is odd
    else:
        if high % 2 == 0:  # both even
            return difference // 2
        else:  # both odd
            return (difference // 2) + 1


def main():
    low = 3
    high = 7
    print(countOdds(low, high))


if __name__ == '__main__':
    main()