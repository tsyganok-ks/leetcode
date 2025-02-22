def isMonotonic(nums):
    """
    Check if array either monotone increasing or monotone decreasing
    :param nums: array
    :return: True or False
    """
    if len(nums) == 1:
        return True

    dec = 0
    inc = 0
    equal = 0
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            inc += 1
        elif nums[i] < nums[i + 1]:
            dec += 1
        else:
            equal += 1

    return True if ((dec == 0 and (inc + equal) != 0) or \
                    (inc == 0 and (dec + equal) != 0)) \
        else False


def main():
    nums = [1, 2, 2, 3]
    print(isMonotonic(nums))


if __name__ == '__main__':
    main()