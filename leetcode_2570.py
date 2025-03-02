def mergeArrays(nums1, nums2):
    """
    Merges 2 arrays. Both arrays follows next pattern: nums = [[idx, num], ...].
    If idx is in both arrays, then we summ numbers, otherwise add without changes.
    :param nums1: first array
    :param nums2: second array
    :return: merged array
    """
    answ_dict = {x: y for x,y in nums1}

    for x, y in nums2:
        if x in answ_dict:
            answ_dict[x] += y
        else:
            answ_dict[x] = y

    answ = [[x, answ_dict[x]] for x in sorted(answ_dict.keys())]

    return answ


def main():
    nums1 = [[2,4],[3,6],[5,5]]
    nums2 = [[1,3],[4,3]]
    print(mergeArrays(nums1, nums2))


if __name__ == '__main__':
    main()