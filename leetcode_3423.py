def maxAdjacentDistance(nums):
    """
    Find the maximum absolute difference between adjacent elements
    :param nums: circular array (the first and last elements are adjacent)
    :return: maximum number
    """
    max_num = 0
    for i in range(len(nums)):
        if abs(nums[i] - nums[i - 1]) > max_num:
            max_num = abs(nums[i] - nums[i - 1])

    return max_num


def main():
    nums = [1, 2, 4]
    print(maxAdjacentDistance(nums))


if __name__ == '__main__':
    main()