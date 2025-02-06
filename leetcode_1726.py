def tupleSameProduct(nums):
    """
    Count the number of tuples (a, b, c, d) such that a * b = c * d,
    where a, b, c, and d are elements of nums, and a != b != c != d
    :param nums: array
    :return: number of tuples
    """
    freq = {}
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] * nums[j] not in freq:
                freq[nums[i] * nums[j]] = 1
            else:
                freq[nums[i] * nums[j]] += 1

    answ = 0

    iter = filter(lambda x: x > 1, freq.values())
    for val in iter:
        answ += val * (val - 1) * 4

    return answ


def main():
    nums = [2, 3, 4, 6]
    print(tupleSameProduct(nums))


if __name__ == '__main__':
    main()