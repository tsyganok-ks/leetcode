def check(nums):
    """
    Check if the array was originally sorted in non-decreasing order,
    then rotated some number
    :param nums: array
    :return: True or False
    """
    for i in range(1, len(nums)):
        if nums[i - 1] > nums[i]:
            orig = nums[i:] + nums[:i]
            for n in range(1, len(orig)):
                if orig[n - 1] > orig[n]:
                    break
            else:
                return True
            return False
    return True


def main():
    nums = [3, 4, 5, 1, 2]
    print(check(nums))


if __name__ == '__main__':
    main()