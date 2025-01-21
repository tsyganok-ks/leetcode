def searchInsert(nums, target):
    """
    Search index to insert target or it's index in nums
    :param nums: sorted array
    :param target: target num
    :return: current index or index to insert
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
    if nums[mid] > target:
        return mid
    else:
        return mid + 1


def main():
    nums = [1, 3, 5, 6]
    target = 2
    print(searchInsert(nums, target))


if __name__ == '__main__':
    main()