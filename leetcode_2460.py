def applyOperations(nums):
    """
    Changes array according to rule: if nums[i] == nums[i+1],
    then multiple nums[i] and makes nums[i+1] = 0.
    After that, moves all zeros to the end of the array.
    :param nums: array
    :return: changed array
    """
    i = 0
    count_nulls = 0
    while i < len(nums)-1:
        if nums[i] == 0:
            nums.pop(i)
            count_nulls += 1
        elif nums[i] == nums[i+1]:
            nums[i] = nums[i] * 2
            nums.pop(i+1)
            count_nulls += 1
            i = i + 1
        else:
            i = i + 1

    return nums + ([0] * count_nulls)


def main():
    nums = [847,847,0,0,0,399,416,416,879,879,206,206,206,272]
    print(applyOperations(nums))


if __name__ == '__main__':
    main()