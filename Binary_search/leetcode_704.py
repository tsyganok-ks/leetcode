def search(nums, target):
    """
    Classic binary search index of target num in nums
    :param nums: array of nums
    :param target: target number
    :return: index of target
    """
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1


def main():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 13
    print(search(nums, target))


if __name__ == '__main__':
    main()
