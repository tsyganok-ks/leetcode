def longestMonotonicSubarray(nums):
    """
    Find len of longest increasing or decreasing subarray
    :param nums: array
    :return: len
    """
    inc = 1
    dec = 1
    answ = 1
    for i in range(1, len(nums)):
        if nums[i - 1] < nums[i]:
            inc += 1
            answ = max(answ, dec)
            dec = 1
        elif nums[i - 1] > nums[i]:
            dec += 1
            answ = max(answ, inc)
            inc = 1
        else:
            answ = max(answ, inc)
            answ = max(answ, dec)
            inc = 1
            dec = 1
    answ = max(answ, dec)
    answ = max(answ, inc)
    return answ


def main():
    nums = [1, 4, 3, 3, 2]
    print(longestMonotonicSubarray(nums))


if __name__ == '__main__':
    main()