def maxAbsoluteSum(nums):
    """
    Calculate the maximum absolute sum of any (possibly empty) subarray of nums
    :param nums: array
    :return: max absolute sum
    """
    max_sum = 0
    min_sum = 0
    prefix_sum = 0

    for num in nums:
        prefix_sum += num

        if prefix_sum > max_sum:
            max_sum = prefix_sum
        if prefix_sum < min_sum:
            min_sum = prefix_sum

    return max_sum - min_sum


def main():
    nums = [2,-5,1,-4,3,-2]
    print(maxAbsoluteSum(nums))


if __name__ == '__main__':
    main()