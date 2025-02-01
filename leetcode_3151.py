def isArraySpecial(nums):
    """
    Check if every pair of array adjacent elements contains two numbers with different parity
    :param nums: array
    :return: True or False
    """
    if len(nums) < 2:
        return True
    else:
        for x in range(1, len(nums)):
            if (nums[x - 1] + nums[x]) % 2 != 1:
                return False
        return True


def main():
    nums = [2, 1, 4]
    print(isArraySpecial(nums))


if __name__ == '__main__':
    main()