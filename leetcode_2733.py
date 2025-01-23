def findNonMinOrMax(nums):
    """
    Find any number which neither minimum and maximum
    :param nums: array of nums
    :return: number
    """
    if len(nums) < 3:
        return -1
    return sorted(nums)[1]