def maxAscendingSum(nums):
    """
    Count the maximum possible sum of an ascending subarray in nums
    :param nums: array
    :return: sum
    """
    tmp_sum = nums[0]
    summ = 0
    for i in range(1, len(nums)):
        if nums[i - 1] < nums[i]:
            tmp_sum += nums[i]
        else:
            summ = max(summ, tmp_sum)
            tmp_sum = nums[i]

    return max(summ, tmp_sum)


def main():
    nums = [10, 20, 30, 5, 10, 50]
    print(maxAscendingSum(nums))


if __name__ == '__main__':
    main()