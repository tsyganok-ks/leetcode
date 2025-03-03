def pivotArray(nums, pivot):
    """
    Return array, where all numbers less than pivot is at the left,
    equal pivot is in the middle, and greater is at the right.
    Order of numbers must be saved.
    :param nums: array
    :param pivot: pivot number
    :return: new array
    """
    equal = []
    list_less = []
    list_more = []
    for num in nums:
        if num == pivot:
            equal.append(num)
        elif num < pivot:
            list_less.append(num)
        else:
            list_more.append(num)
    return list_less + equal + list_more


def main():
    nums = [9, 12, 5, 10, 14, 3, 10]
    pivot = 10
    print(pivotArray(nums, pivot))


if __name__ == '__main__':
    main()