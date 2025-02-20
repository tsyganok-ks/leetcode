def findDifferentBinaryString(nums):
    '''
    Find any string with len(n), which does not appear in nums
    :param nums: array
    :return: any binary number
    '''
    n = len(nums[0])
    dec_nums = [int(x, 2) for x in nums]
    s = ''
    for i in range(2**n):
        if i not in dec_nums:
            s = str(bin(i))[2:]
            if len(s) < n:
                s = '0' * (n - len(s)) + s
            break
    return s


def main():
    nums = ["10","01"]
    print(findDifferentBinaryString(nums))


if __name__ == '__main__':
    main()