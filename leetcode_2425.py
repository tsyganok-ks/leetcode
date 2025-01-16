from functools import reduce

def xorAllNums(nums1, nums2):
    """
    Calc XOR between all nums in nums1 and nums2
    :param nums1: list of nums
    :param nums2: list of nums
    :return: result or XOR
    """
    xor_n1 = 0
    xor_n2 = 0
    if len(nums2) % 2 != 0:
        xor_n1 = reduce(lambda x, y: x^y, nums1)
    if len(nums1) % 2 != 0:
        xor_n2 = reduce(lambda x, y: x^y, nums2)

    return xor_n2 ^ xor_n1



def main():
    nums1 = [2, 1, 3]
    nums2 = [10, 2, 5, 0]
    print(xorAllNums(nums1, nums2))


if __name__ == '__main__':
    main()